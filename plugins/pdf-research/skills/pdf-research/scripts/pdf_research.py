#!/usr/bin/env python3
"""
PDF Research CLI - Unified interface for indexing and searching PDFs.

Usage:
    python pdf_research.py index <pdf_dir> [--storage <path>]
    python pdf_research.py search <query> [--mode <mode>] [--storage <path>]
    python pdf_research.py status [--storage <path>]
    python pdf_research.py config --pdf-dir <path> --storage-dir <path>
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

# Add scripts directory to path
SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "config.json"


def load_config():
    """Load configuration from config.json."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {
        "pdf_dir": "",
        "storage_dir": "",
        "auto_index": True,
        "search_mode": "hybrid"
    }


def save_config(config):
    """Save configuration to config.json."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Configuration saved to {CONFIG_FILE}")


def get_paths(args, config):
    """Get PDF and storage paths from args, config, or environment."""
    pdf_dir = getattr(args, 'pdf_dir', None) or config.get('pdf_dir') or os.getenv('PDF_RESEARCH_DIR', '')
    storage_dir = getattr(args, 'storage', None) or config.get('storage_dir') or os.getenv('PDF_RESEARCH_STORAGE', '')

    if not storage_dir:
        storage_dir = str(SCRIPT_DIR / "rag_storage")

    return pdf_dir, storage_dir


async def cmd_index(args, config):
    """Index PDF files."""
    from index_pdfs import index_pdfs

    pdf_dir, storage_dir = get_paths(args, config)

    if not pdf_dir:
        print("Error: PDF directory not specified.")
        print("Use: python pdf_research.py index <pdf_dir>")
        print("Or configure with: python pdf_research.py config --pdf-dir <path>")
        return 1

    pdf_path = Path(pdf_dir).resolve()
    storage_path = Path(storage_dir).resolve()

    if not pdf_path.exists():
        print(f"Error: PDF directory not found: {pdf_path}")
        return 1

    await index_pdfs(pdf_path, storage_path)

    # Update config with used paths
    config['pdf_dir'] = str(pdf_path)
    config['storage_dir'] = str(storage_path)
    save_config(config)

    return 0


async def cmd_search(args, config):
    """Search indexed PDFs."""
    from search import search, interactive_search

    _, storage_dir = get_paths(args, config)
    storage_path = Path(storage_dir).resolve()

    if not storage_path.exists():
        print(f"Error: No indexed data found at {storage_path}")
        print("Run indexing first: python pdf_research.py index <pdf_dir>")
        return 1

    mode = args.mode or config.get('search_mode', 'hybrid')

    if args.query:
        query = " ".join(args.query)
        result = await search(query, storage_path, mode)
        print(result)
    else:
        await interactive_search(storage_path)

    return 0


def cmd_status(args, config):
    """Show indexing status."""
    _, storage_dir = get_paths(args, config)
    storage_path = Path(storage_dir).resolve()

    print("=" * 60)
    print("  PDF Research Status")
    print("=" * 60)

    # Show config
    print(f"\nConfiguration:")
    print(f"  PDF Directory: {config.get('pdf_dir') or '(not set)'}")
    print(f"  Storage Directory: {storage_dir}")
    print(f"  Search Mode: {config.get('search_mode', 'hybrid')}")
    print(f"  Auto Index: {config.get('auto_index', True)}")

    # Check storage
    if not storage_path.exists():
        print(f"\nStorage Status: Not initialized")
        print("Run indexing first: python pdf_research.py index <pdf_dir>")
        return 0

    # Count documents
    docs_file = storage_path / "kv_store_full_docs.json"
    chunks_file = storage_path / "kv_store_text_chunks.json"
    entities_file = storage_path / "kv_store_full_entities.json"

    doc_count = 0
    chunk_count = 0
    entity_count = 0
    doc_names = []

    if docs_file.exists():
        with open(docs_file) as f:
            data = json.load(f)
            doc_count = len(data)
            for doc_id, content in data.items():
                if "[Document: " in content:
                    start = content.find("[Document: ") + len("[Document: ")
                    end = content.find("]", start)
                    if end > start:
                        doc_names.append(content[start:end])

    if chunks_file.exists():
        with open(chunks_file) as f:
            chunk_count = len(json.load(f))

    if entities_file.exists():
        with open(entities_file) as f:
            entity_count = len(json.load(f))

    # Calculate size
    total_size = sum(f.stat().st_size for f in storage_path.glob("*") if f.is_file())
    size_mb = total_size / (1024 * 1024)

    print(f"\nStorage Status:")
    print(f"  Documents: {doc_count}")
    print(f"  Chunks: {chunk_count}")
    print(f"  Entities: {entity_count}")
    print(f"  Size: {size_mb:.2f} MB")

    if doc_names:
        print(f"\nIndexed Documents:")
        for name in sorted(doc_names)[:10]:
            print(f"  - {name}")
        if len(doc_names) > 10:
            print(f"  ... and {len(doc_names) - 10} more")

    print("=" * 60)
    return 0


def cmd_config(args, config):
    """Update configuration."""
    if args.pdf_dir:
        config['pdf_dir'] = str(Path(args.pdf_dir).resolve())
    if args.storage_dir:
        config['storage_dir'] = str(Path(args.storage_dir).resolve())
    if args.mode:
        config['search_mode'] = args.mode

    save_config(config)

    print("\nCurrent Configuration:")
    print(f"  PDF Directory: {config.get('pdf_dir') or '(not set)'}")
    print(f"  Storage Directory: {config.get('storage_dir') or '(not set)'}")
    print(f"  Search Mode: {config.get('search_mode', 'hybrid')}")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="PDF Research - Index and search PDF documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Configure default paths
  python pdf_research.py config --pdf-dir ~/Documents/papers --storage-dir ./rag_storage

  # Index PDFs
  python pdf_research.py index ~/Documents/papers

  # Search (single query)
  python pdf_research.py search "What is machine learning?"

  # Search (interactive mode)
  python pdf_research.py search

  # Check status
  python pdf_research.py status
"""
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Index command
    index_parser = subparsers.add_parser('index', help='Index PDF files')
    index_parser.add_argument('pdf_dir', nargs='?', help='Directory containing PDFs')
    index_parser.add_argument('--storage', '-s', help='Storage directory for index')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search indexed PDFs')
    search_parser.add_argument('query', nargs='*', help='Search query (omit for interactive)')
    search_parser.add_argument('--mode', '-m', choices=['naive', 'local', 'global', 'hybrid'],
                               help='Search mode')
    search_parser.add_argument('--storage', '-s', help='Storage directory')

    # Status command
    status_parser = subparsers.add_parser('status', help='Show indexing status')
    status_parser.add_argument('--storage', '-s', help='Storage directory')

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure default settings')
    config_parser.add_argument('--pdf-dir', help='Default PDF directory')
    config_parser.add_argument('--storage-dir', help='Default storage directory')
    config_parser.add_argument('--mode', choices=['naive', 'local', 'global', 'hybrid'],
                               help='Default search mode')

    args = parser.parse_args()
    config = load_config()

    if not args.command:
        parser.print_help()
        return 0

    if args.command == 'index':
        return asyncio.run(cmd_index(args, config))
    elif args.command == 'search':
        return asyncio.run(cmd_search(args, config))
    elif args.command == 'status':
        return cmd_status(args, config)
    elif args.command == 'config':
        return cmd_config(args, config)

    return 0


if __name__ == "__main__":
    sys.exit(main())
