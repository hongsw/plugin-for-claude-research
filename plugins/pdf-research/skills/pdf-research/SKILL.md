# PDF Research Skill

LightRAG-based PDF document indexing and semantic search for Claude Code research workflows.

## Quick Start (For Claude)

When user invokes `/pdf-research`, Claude should:

1. **Check status first**: Run `python pdf_research.py status` to see current configuration
2. **Auto-index if requested**: When user provides a PDF directory, run indexing automatically
3. **Search queries**: Execute searches and return formatted results

### Automatic Workflow

```bash
# Always run from scripts directory
cd ~/.claude/skills/pdf-research/scripts

# Check current status
python pdf_research.py status

# Index PDFs (when user provides a directory)
python pdf_research.py index /path/to/pdfs

# Search (single query)
python pdf_research.py search "user's question" --mode hybrid

# Interactive search session
python pdf_research.py search
```

### Environment Requirements

Before running commands, ensure:
```bash
# Activate Python environment with dependencies
source /path/to/venv/bin/activate  # or use system Python with deps installed

# Ensure OpenAI API key is set
export OPENAI_API_KEY=sk-...
```

## Core Capabilities

### 1. PDF Indexing (`index` command)
- Extracts text from PDF documents using PyMuPDF
- Creates semantic chunks with metadata
- Builds knowledge graph with entities and relationships
- Generates vector embeddings for semantic search
- Supports incremental indexing (only new files)

### 2. Semantic Search (`search` command)
- **naive**: Simple keyword matching
- **local**: Focus on specific entities and details
- **global**: Focus on broad themes and summaries
- **hybrid**: Combined local + global (recommended)

### 3. Status Check (`status` command)
- Shows current configuration
- Lists indexed documents
- Reports storage statistics

### 4. Configuration (`config` command)
- Set default PDF directory
- Set default storage directory
- Set default search mode

## Claude Integration Protocol

### When User Says "Index PDFs" or Provides a Path

1. Verify the path exists
2. Run: `python pdf_research.py index <path>`
3. Report results (documents indexed, chunks created, storage size)

### When User Asks a Question About Documents

1. Check if storage exists: `python pdf_research.py status`
2. If not indexed, ask user for PDF directory
3. Run search: `python pdf_research.py search "<question>"`
4. Format and present results with source references

### When User Wants to Configure

1. Run: `python pdf_research.py config --pdf-dir <path> --storage-dir <path>`
2. Confirm configuration saved

## Command Reference

```bash
# Configure defaults (run once)
python pdf_research.py config --pdf-dir /path/to/pdfs --storage-dir ./rag_storage

# Index PDFs
python pdf_research.py index [pdf_dir] [--storage <path>]

# Search (single query)
python pdf_research.py search "query" [--mode hybrid|local|global|naive]

# Search (interactive)
python pdf_research.py search

# Check status
python pdf_research.py status
```

## Search Modes

| Mode | Best For | Description |
|------|----------|-------------|
| `hybrid` | General queries | Combined local + global (default) |
| `local` | Specific facts | Names, numbers, definitions |
| `global` | Summaries | Themes, trends, overviews |
| `naive` | Exact terms | Simple keyword matching |

## Storage Structure

After indexing, `rag_storage/` contains:

| File | Description |
|------|-------------|
| `config.json` | User configuration |
| `kv_store_full_docs.json` | Full document text |
| `kv_store_text_chunks.json` | Semantic chunks |
| `kv_store_full_entities.json` | Extracted entities |
| `vdb_*.json` | Vector embeddings |
| `graph_*.graphml` | Knowledge graph |

## Example Session

```
User: /pdf-research ~/Documents/papers 인덱싱해줘

Claude: [Runs indexing]
        Indexing complete!
        - Documents: 5
        - Chunks: 247
        - Storage: 32.5 MB

User: AI 인재 양성 전략에 대해 알려줘

Claude: [Runs search]
        Based on the indexed documents...
        [Detailed response with references]
```

## Troubleshooting

### "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY=sk-your-key
```

### "No indexed data found"
```bash
python pdf_research.py index /path/to/pdfs
```

### "Module not found" errors
```bash
pip install lightrag-hku[api] pymupdf python-dotenv
```

## Dependencies

- Python 3.10+
- `lightrag-hku[api]>=1.4.9`
- `pymupdf>=1.24.0`
- `python-dotenv>=1.0.0`
- OpenAI API key
