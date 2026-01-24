#!/usr/bin/env python3
"""
PDF Search Interface for LightRAG
Query indexed PDFs using natural language.

Usage:
    python search.py [query] [--mode <mode>] [--storage-dir <path>]

Search Modes:
    naive  - Simple keyword matching
    local  - Focus on specific entities/details
    global - Focus on broad themes/summaries
    hybrid - Combines local and global (default, recommended)

Environment:
    OPENAI_API_KEY: Required for embeddings and LLM
    PDF_RESEARCH_STORAGE: Default storage directory (optional)
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

# Load environment variables
load_dotenv()


async def search(query: str, storage_dir: Path, mode: str = "hybrid") -> str:
    """
    Search indexed PDFs with a natural language query.

    Args:
        query: Natural language search query
        storage_dir: Path to the RAG storage directory
        mode: Search mode - 'naive', 'local', 'global', or 'hybrid' (default)
    """
    if not os.getenv("OPENAI_API_KEY"):
        return "Error: OPENAI_API_KEY not set."

    if not storage_dir.exists():
        return f"Error: No indexed data found at {storage_dir}. Run index_pdfs.py first."

    rag = LightRAG(
        working_dir=str(storage_dir),
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )

    await rag.initialize_storages()

    result = await rag.aquery(
        query,
        param=QueryParam(mode=mode)
    )

    await rag.finalize_storages()

    return result


def get_storage_info(storage_dir: Path) -> dict:
    """Get information about the indexed storage."""
    info = {
        "exists": storage_dir.exists(),
        "documents": 0,
        "document_names": []
    }

    if not storage_dir.exists():
        return info

    docs_file = storage_dir / "kv_store_full_docs.json"
    if docs_file.exists():
        try:
            with open(docs_file) as f:
                data = json.load(f)
            info["documents"] = len(data)

            # Extract document names
            for doc_id, content in data.items():
                if "[Document: " in content:
                    start = content.find("[Document: ") + len("[Document: ")
                    end = content.find("]", start)
                    if end > start:
                        info["document_names"].append(content[start:end])
        except Exception:
            pass

    return info


async def interactive_search(storage_dir: Path):
    """Interactive search mode."""
    print("=" * 60)
    print("  LightRAG PDF Search System")
    print("  Claude Code PDF Research Plugin")
    print("=" * 60)

    # Show storage info
    info = get_storage_info(storage_dir)
    if not info["exists"]:
        print(f"\nError: No indexed data found at {storage_dir}")
        print("Run 'python index_pdfs.py --pdf-dir <path>' first.")
        return

    print(f"\nStorage: {storage_dir}")
    print(f"Indexed Documents: {info['documents']}")
    if info["document_names"]:
        print("\nAvailable documents:")
        for name in sorted(info["document_names"])[:10]:
            print(f"  - {name}")
        if len(info["document_names"]) > 10:
            print(f"  ... and {len(info['document_names']) - 10} more")

    print("\n" + "-" * 60)
    print("Search modes: naive, local, global, hybrid (default)")
    print("Commands: /mode <mode>, /docs, /info, /quit, /help")
    print("-" * 60)

    current_mode = "hybrid"

    if not os.getenv("OPENAI_API_KEY"):
        print("\nError: OPENAI_API_KEY not set.")
        return

    # Initialize RAG once for the session
    rag = LightRAG(
        working_dir=str(storage_dir),
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )
    await rag.initialize_storages()

    try:
        while True:
            try:
                query = input(f"\n[{current_mode}] Query: ").strip()
            except EOFError:
                break

            if not query:
                continue

            if query.lower() == "/quit":
                break

            if query.lower() == "/help":
                print("\nCommands:")
                print("  /mode naive  - Simple keyword matching")
                print("  /mode local  - Focus on specific details")
                print("  /mode global - Focus on broad themes")
                print("  /mode hybrid - Combined approach (recommended)")
                print("  /docs        - List indexed documents")
                print("  /info        - Show storage statistics")
                print("  /quit        - Exit the search")
                continue

            if query.lower() == "/docs":
                print("\nIndexed Documents:")
                for name in sorted(info["document_names"]):
                    print(f"  - {name}")
                continue

            if query.lower() == "/info":
                print(f"\nStorage: {storage_dir}")
                print(f"Documents: {info['documents']}")
                print(f"Mode: {current_mode}")
                continue

            if query.lower().startswith("/mode "):
                new_mode = query[6:].strip().lower()
                if new_mode in ["naive", "local", "global", "hybrid"]:
                    current_mode = new_mode
                    print(f"Mode changed to: {current_mode}")
                else:
                    print("Invalid mode. Use: naive, local, global, or hybrid")
                continue

            print("\nSearching...\n")
            result = await rag.aquery(
                query,
                param=QueryParam(mode=current_mode)
            )
            print("-" * 60)
            print(result)
            print("-" * 60)

    finally:
        await rag.finalize_storages()
        print("\nGoodbye!")


async def single_query(query: str, storage_dir: Path, mode: str = "hybrid"):
    """Single query mode for CLI usage."""
    result = await search(query, storage_dir, mode)
    print(result)


def main():
    parser = argparse.ArgumentParser(
        description="Search indexed PDFs with natural language queries"
    )
    parser.add_argument(
        "query",
        nargs="*",
        help="Search query (omit for interactive mode)"
    )
    parser.add_argument(
        "--mode", "-m",
        choices=["naive", "local", "global", "hybrid"],
        default="hybrid",
        help="Search mode (default: hybrid)"
    )
    parser.add_argument(
        "--storage-dir", "-s",
        type=str,
        default=os.getenv("PDF_RESEARCH_STORAGE", "./rag_storage"),
        help="Directory containing the RAG index"
    )

    args = parser.parse_args()
    storage_dir = Path(args.storage_dir).resolve()

    if args.query:
        query = " ".join(args.query)
        asyncio.run(single_query(query, storage_dir, args.mode))
    else:
        asyncio.run(interactive_search(storage_dir))


if __name__ == "__main__":
    main()
