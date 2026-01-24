#!/usr/bin/env python3
"""
PDF Indexing Script for LightRAG
Extracts text from PDFs and indexes them into LightRAG for semantic search.

Usage:
    python index_pdfs.py [--pdf-dir <path>] [--storage-dir <path>]

Environment:
    OPENAI_API_KEY: Required for embeddings and LLM
    PDF_RESEARCH_DIR: Default PDF directory (optional)
    PDF_RESEARCH_STORAGE: Default storage directory (optional)
"""

import argparse
import asyncio
import json
import logging
import os
import sys
import threading
import time
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF
from dotenv import load_dotenv
from lightrag import LightRAG
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

# Load environment variables
load_dotenv()

# Suppress LightRAG INFO logs
logging.getLogger("lightrag").setLevel(logging.WARNING)
logging.getLogger("nano-vectordb").setLevel(logging.WARNING)


class ProgressIndicator:
    """Blinking dot progress indicator."""

    def __init__(self):
        self.running = False
        self.thread = None

    def start(self, prefix=""):
        self.running = True
        self.prefix = prefix
        self.thread = threading.Thread(target=self._animate, daemon=True)
        self.thread.start()

    def _animate(self):
        dots = [".", "..", "...", "...."]
        idx = 0
        while self.running:
            sys.stdout.write(f"\r{self.prefix} {dots[idx % len(dots)]}   ")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.3)

    def stop(self, final_message=""):
        self.running = False
        if self.thread:
            self.thread.join(timeout=0.5)
        sys.stdout.write(f"\r{' ' * 80}\r")  # Clear line
        if final_message:
            print(final_message)
        sys.stdout.flush()


def extract_text_from_pdf(pdf_path: Path) -> Optional[str]:
    """Extract text content from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text_parts = []

        for page_num, page in enumerate(doc, 1):
            text = page.get_text()
            if text.strip():
                text_parts.append(f"[Page {page_num}]\n{text}")

        doc.close()

        if text_parts:
            # Add metadata header
            full_text = f"[Document: {pdf_path.name}]\n\n" + "\n\n".join(text_parts)
            return full_text
        return None

    except Exception as e:
        print(f"Error extracting {pdf_path.name}: {e}")
        return None


def get_indexed_docs(storage_dir: Path) -> set:
    """Get list of already indexed document names."""
    status_file = storage_dir / "kv_store_full_docs.json"
    if not status_file.exists():
        return set()

    try:
        with open(status_file) as f:
            data = json.load(f)
        # Extract document names from the stored data
        indexed = set()
        for doc_id, content in data.items():
            if "[Document: " in content:
                start = content.find("[Document: ") + len("[Document: ")
                end = content.find("]", start)
                if end > start:
                    indexed.add(content[start:end])
        return indexed
    except Exception:
        return set()


def get_storage_stats(storage_dir: Path) -> dict:
    """Get statistics about the indexed storage."""
    stats = {
        "total_docs": 0,
        "total_chunks": 0,
        "total_entities": 0,
        "storage_size_mb": 0
    }

    try:
        # Count documents
        docs_file = storage_dir / "kv_store_full_docs.json"
        if docs_file.exists():
            with open(docs_file) as f:
                data = json.load(f)
                stats["total_docs"] = len(data)

        # Count chunks
        chunks_file = storage_dir / "kv_store_text_chunks.json"
        if chunks_file.exists():
            with open(chunks_file) as f:
                data = json.load(f)
                stats["total_chunks"] = len(data)

        # Count entities
        entities_file = storage_dir / "kv_store_full_entities.json"
        if entities_file.exists():
            with open(entities_file) as f:
                data = json.load(f)
                stats["total_entities"] = len(data)

        # Calculate storage size
        total_size = 0
        for file in storage_dir.glob("*"):
            if file.is_file():
                total_size += file.stat().st_size
        stats["storage_size_mb"] = round(total_size / (1024 * 1024), 2)

    except Exception:
        pass

    return stats


async def index_pdfs(pdf_dir: Path, storage_dir: Path):
    """Index all PDFs in the specified directory."""

    # Verify API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set.")
        print("Please set it in your environment or .env file.")
        return

    # Verify PDF directory exists
    if not pdf_dir.exists():
        print(f"Error: PDF directory not found: {pdf_dir}")
        return

    # Create storage directory
    storage_dir.mkdir(parents=True, exist_ok=True)

    # Check already indexed docs
    indexed_docs = get_indexed_docs(storage_dir)

    print("=" * 60)
    print("  LightRAG PDF Indexing for Claude Code")
    print("=" * 60)
    print(f"PDF Directory: {pdf_dir}")
    print(f"Storage Directory: {storage_dir}")
    print("-" * 60)

    rag = LightRAG(
        working_dir=str(storage_dir),
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )

    await rag.initialize_storages()

    # Find all PDFs
    pdf_files = sorted(pdf_dir.glob("*.pdf"))
    total = len(pdf_files)

    # Filter out already indexed
    pending_files = [p for p in pdf_files if p.name not in indexed_docs]

    print(f"Total PDFs: {total}")
    print(f"Already indexed: {len(indexed_docs)}")
    print(f"Pending: {len(pending_files)}")
    print("-" * 60)

    if not pending_files:
        print("All files are already indexed.")
        stats = get_storage_stats(storage_dir)
        print(f"\nStorage Statistics:")
        print(f"  Documents: {stats['total_docs']}")
        print(f"  Chunks: {stats['total_chunks']}")
        print(f"  Entities: {stats['total_entities']}")
        print(f"  Storage Size: {stats['storage_size_mb']} MB")
        await rag.finalize_storages()
        return

    progress = ProgressIndicator()
    indexed_count = len(indexed_docs)
    failed_count = 0

    for i, pdf_path in enumerate(pending_files, 1):
        # Start progress indicator
        display_name = pdf_path.name[:40] + "..." if len(pdf_path.name) > 40 else pdf_path.name
        progress.start(f"[{indexed_count + i}/{total}] {display_name}")

        text = extract_text_from_pdf(pdf_path)
        if text:
            try:
                await rag.ainsert(text)
                progress.stop(f"[{indexed_count + i}/{total}] {display_name}")
            except Exception as e:
                progress.stop(f"[{indexed_count + i}/{total}] {display_name} - Error: {str(e)[:30]}")
                failed_count += 1
        else:
            progress.stop(f"[{indexed_count + i}/{total}] {display_name} - No text extracted")
            failed_count += 1

    await rag.finalize_storages()

    # Final statistics
    stats = get_storage_stats(storage_dir)

    print("-" * 60)
    print("Indexing Complete!")
    print(f"  Succeeded: {len(pending_files) - failed_count}")
    print(f"  Failed: {failed_count}")
    print(f"  Total Indexed: {indexed_count + len(pending_files) - failed_count}")
    print(f"\nStorage Statistics:")
    print(f"  Documents: {stats['total_docs']}")
    print(f"  Chunks: {stats['total_chunks']}")
    print(f"  Entities: {stats['total_entities']}")
    print(f"  Storage Size: {stats['storage_size_mb']} MB")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Index PDF files for LightRAG semantic search"
    )
    parser.add_argument(
        "--pdf-dir",
        type=str,
        default=os.getenv("PDF_RESEARCH_DIR", "./pdfs"),
        help="Directory containing PDF files to index"
    )
    parser.add_argument(
        "--storage-dir",
        type=str,
        default=os.getenv("PDF_RESEARCH_STORAGE", "./rag_storage"),
        help="Directory to store the RAG index"
    )

    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir).resolve()
    storage_dir = Path(args.storage_dir).resolve()

    asyncio.run(index_pdfs(pdf_dir, storage_dir))


if __name__ == "__main__":
    main()
