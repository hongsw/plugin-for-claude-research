# PDF Research Plugin

LightRAG-based PDF document indexing and semantic search for Claude Code research workflows.

## Overview

This plugin enables Claude Code to index PDF documents and perform semantic search using LightRAG. It creates a knowledge graph and vector embeddings from your PDF files, allowing for intelligent query responses.

## Features

- **PDF Text Extraction**: Extracts text from PDF documents with page-level metadata
- **Semantic Indexing**: Creates vector embeddings and knowledge graphs
- **Multi-Mode Search**: Supports naive, local, global, and hybrid search modes
- **Incremental Indexing**: Only indexes new files, preserving existing index
- **Interactive & CLI Modes**: Both interactive sessions and single-query CLI

## Requirements

- Python 3.10+
- OpenAI API key
- Claude Code CLI

## Installation

### Via Claude Code Plugin System

```bash
# Add the plugin repository
/plugin marketplace add hongsw/plugin-for-claude-research

# Install the pdf-research plugin
/plugin install pdf-research
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/hongsw/plugin-for-claude-research
cd plugin-for-claude-research/plugins/pdf-research

# Run installation
node bin/install.js

# Install Python dependencies
cd ~/.claude/skills/pdf-research/scripts
pip install -r requirements.txt
```

## Configuration

Set your OpenAI API key:

```bash
export OPENAI_API_KEY=sk-your-api-key
```

Optional environment variables:
- `PDF_RESEARCH_DIR`: Default PDF directory
- `PDF_RESEARCH_STORAGE`: Default storage directory

## Usage

### Indexing PDFs

```bash
cd ~/.claude/skills/pdf-research/scripts

# Index PDFs in a specific directory
python index_pdfs.py --pdf-dir /path/to/pdfs --storage-dir ./rag_storage
```

### Searching

**Single Query:**
```bash
python search.py "What are the main findings about neural networks?" --mode hybrid
```

**Interactive Mode:**
```bash
python search.py
```

### Search Modes

| Mode | Description | Best For |
|------|-------------|----------|
| `naive` | Simple keyword matching | Exact terms |
| `local` | Entity-focused search | Specific facts, names, numbers |
| `global` | Theme-focused search | Summaries, trends |
| `hybrid` | Combined approach | General queries (recommended) |

## Claude Code Integration

Once installed, you can use these prompts in Claude Code:

- **index-pdfs**: Guide for indexing PDF documents
- **search-query**: Execute semantic searches
- **research-assistant**: Comprehensive research sessions

## Storage Structure

After indexing, the storage directory contains:

```
rag_storage/
├── kv_store_full_docs.json      # Full document text
├── kv_store_text_chunks.json    # Semantic chunks
├── kv_store_full_entities.json  # Extracted entities
├── kv_store_full_relations.json # Entity relationships
├── vdb_chunks.json              # Chunk embeddings
├── vdb_entities.json            # Entity embeddings
└── graph_chunk_entity_relation.graphml  # Knowledge graph
```

## Example Workflow

```
# In Claude Code session

User: "Index my research papers in ~/Documents/papers"

Claude: Running PDF indexing...
        [1/10] paper1.pdf - Done
        [2/10] paper2.pdf - Done
        ...
        Indexing complete. 10 documents indexed.

User: "What are the key findings about transformer architectures?"

Claude: Based on the indexed documents...
        [Comprehensive response with source references]
```

## Troubleshooting

### "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY=sk-your-key
```

### "No indexed data found"
Run the indexing script first:
```bash
python index_pdfs.py --pdf-dir /your/pdf/directory
```

### "Text extraction failed"
- Ensure PDFs contain selectable text (not scanned images)
- For scanned documents, use OCR preprocessing

## Dependencies

- `lightrag-hku[api]>=1.4.9` - LightRAG framework
- `pymupdf>=1.24.0` - PDF text extraction
- `python-dotenv>=1.0.0` - Environment configuration

## License

MIT
