# Domain Research Plugin

Universal research framework with conversational intent analysis for Claude Code.

## Features

- **Conversational Discovery**: Natural dialogue to define research context
- **Field-Agnostic**: Works for any domain (Manufacturing AI, Healthcare, FinTech, etc.)
- **5-Step Pipeline**: Systematic progression from questions to action plans
- **Practitioner Focus**: Designed for domain experts, not academics

## Installation

```bash
# Add the marketplace
/plugin marketplace add hongsw/plugin-for-claude-research

# Install this plugin
/plugin install domain-research
```

## Usage

After installation, start a research conversation:

```
You: "I want to research AI for healthcare"

Claude: "That's a broad space. Let me understand better:
        - Are you in the healthcare industry?
        - Clinical, administrative, or research focus?"
```

## Available Prompts

| Prompt | Purpose |
|--------|---------|
| intent-analyzer.md | Conversational context building |
| key-questions.md | Research question generation |
| research-gaps.md | Gap identification |
| insight-extraction.md | Source analysis |
| multi-source-synthesis.md | Multi-source integration |
| practical-application.md | Action planning |
| comprehensive-guide.md | Final roadmap |

## License

MIT
