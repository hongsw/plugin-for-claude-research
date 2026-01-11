```
   _____ _                 _        ____                               _
  / ____| |               | |      |  _ \                             | |
 | |    | | __ _ _   _  __| | ___  | |_) | ___  ___  ___  __ _ _ __ __| |__
 | |    | |/ _` | | | |/ _` |/ _ \ |  _ < / _ \/ __|/ _ \/ _` | '__/ __| '_ \
 | |____| | (_| | |_| | (_| |  __/ | |_) |  __/\__ \  __/ (_| | | | (__| | | |
  \_____|_|\__,_|\__,_|\__,_|\___| |____/ \___||___/\___|\__,_|_|  \___|_| |_|

  ╔═══════════════════════════════════════════════════════════════════════╗
  ║  🔬 Conversation → Context → Questions → Gaps → Insights → Action 🎯  ║
  ╚═══════════════════════════════════════════════════════════════════════╝
```

# Claude Research Framework

> **한국어 안내**
> 이 플러그인은 Claude Code에서 **체계적인 리서치**를 도와주는 도구입니다.
>
> **사용법이 간단합니다:**
> 1. "AI로 품질검사를 개선하고 싶어" 처럼 관심사를 말하면
> 2. 대화를 통해 연구 범위를 좁혀가고
> 3. 5단계 파이프라인으로 실행 가능한 인사이트를 얻습니다
>
> 제조AI, 헬스케어, 핀테크 등 **어떤 분야든** 적용 가능합니다.

---

A **universal research plugin** that guides users from broad exploration to specific domain research through conversational intent analysis. Works for any field.

## Overview

This plugin transforms how you approach research:

1. **Start with a conversation** - Tell us what you're curious about
2. **We'll help you focus** - Through dialogue, not forms
3. **Execute systematic research** - 5-step pipeline to actionable insights
4. **Get practical results** - Research that leads to action

### Works for Any Domain

| Domain | Example Use Case |
|--------|------------------|
| Manufacturing AI | Quality inspection for SMEs |
| Healthcare | Staff scheduling optimization |
| EdTech | AI tutoring implementation |
| FinTech | Blockchain for payments |
| Sustainability | Carbon neutrality pathways |
| HR Tech | AI in recruitment |
| *Your Field* | *Your Topic* |

---

## Key Features

- **Conversational Discovery**: Natural dialogue to define research context
- **Field-Agnostic**: Apply to any domain you bring
- **5-Step Pipeline**: Systematic progression from questions to action plans
- **MCP Integration**: Real-time research augmentation with WebSearch and Sequential
- **Practitioner Focus**: Designed for domain experts, not academics

---

## Installation

### Add Marketplace & Install Plugin

```bash
# Add this marketplace to Claude Code
/plugin marketplace add hongsw/plugin-for-claude-research

# Install the domain-research plugin
/plugin install domain-research
```

That's it! The plugin is now ready to use.

---

## Quick Start

### 1. Start a Research Conversation

```bash
claude
```

```
You: "I'm interested in AI for healthcare"

Claude: "That's a broad space. Let me understand better:
        - Are you in the healthcare industry?
        - Clinical, administrative, or research focus?
        - Is this for a specific project?"

You: "Hospital admin. Looking at scheduling optimization."

Claude: "Got it. AI for hospital staff scheduling.
        - What's the main problem with current scheduling?
        - What's your timeline for implementation?"

[Conversation continues → Research context generated]
```

### 2. Execute Research Pipeline

Once context is established:
```
/research-questions    # Generate 5 key questions
/research-gaps         # Identify research gaps
/research-synthesize   # Integrate findings
/research-action       # Create action plan
```

---

## Directory Structure

```
plugin-for-claude-research/
├── .claude-plugin/
│   ├── plugin.json              # Marketplace metadata
│   └── marketplace.json         # Plugin registry
├── plugins/
│   └── domain-research/         # Main plugin
│       ├── .claude-plugin/
│       │   └── plugin.json      # Plugin config
│       ├── bin/
│       │   └── install.js       # Installation script
│       ├── skills/
│       │   └── domain-research/
│       │       ├── SKILL.md     # Core methodology
│       │       └── prompts/     # Research prompts
│       ├── package.json
│       └── README.md
├── examples/
│   ├── manufacturing-ai-2026/   # Manufacturing example
│   ├── healthcare-scheduling/   # Healthcare example
│   └── fintech-blockchain/      # FinTech example
├── templates/                   # Optional input templates
└── README.md
```

---

## Research Pipeline

### Step 0: Conversational Intent Analysis
**Start with dialogue, not forms.**

- Open invitation to share research interest
- Adaptive questioning based on user clarity
- Synthesis and confirmation
- Structured research context output

### Step 1: Key Question Generation
Generate 5 testable, meaningful research questions with:
- Importance justification
- Potential impact analysis
- Possible methodologies

### Step 2: Research Gap Identification
Identify underexplored areas:
- Literature synthesis
- Methodological limitations
- Emerging opportunities
- 4 priority gaps with research ideas

### Step 3: Key Insight Extraction
Deep analysis of individual sources:
- Research design evaluation
- Key findings extraction
- Practical implications
- Critical assessment

### Step 4: Multi-Source Synthesis
Integrate across sources:
- Common theme identification
- Evidence strength ranking
- Contradiction resolution
- Knowledge gap mapping

### Step 5: Practical Application
Transform to action:
- Consolidated insights
- Executable action items
- Implementation challenges
- KPI definitions

### Final: Comprehensive Guide
Single-page practitioner roadmap with:
- Key findings table
- Action timeline
- Success metrics
- Risk awareness

---

## User Types Supported

### "I know exactly what I want"
```
You: "I want to research computer vision for quality inspection in SMEs"
→ 2-3 clarifying questions → Research context ready
```

### "I have a vague idea"
```
You: "I'm interested in AI for my factory"
→ 4-6 discovery questions → Focused direction → Context ready
```

### "I was told to research this"
```
You: "My boss wants a report on blockchain"
→ Stakeholder questions → Purpose alignment → Context ready
```

### "I'm just exploring"
```
You: "What could AI do for education?"
→ Domain narrowing → Application focus → Context ready
```

---

## Installation

### Method 1: Direct Install from GitHub (Recommended)

```bash
# Install directly from GitHub
claude mcp add-json domain-research '{"type":"stdio","command":"npx","args":["github:hongsw/plugin-for-claude-research"]}'
```

### Method 2: Clone and Install Locally

```bash
# Clone the repository
git clone https://github.com/hongsw/plugin-for-claude-research.git

# Navigate to the directory
cd plugin-for-claude-research

# Add to Claude Code's allowed directories
claude config add-dir .

# Start Claude Code in this directory
claude
```

### Method 3: Add as Working Directory

Simply add the cloned repository to your Claude Code session:

```bash
# Clone first
git clone https://github.com/hongsw/plugin-for-claude-research.git

# Then in Claude Code, add the directory
/add-dir ~/path/to/plugin-for-claude-research
```

### Verify Installation

After installation, the prompts in `skills/domain-research/prompts/` will be available as context for your research sessions.

---

## MCP Server Integration

### WebSearch
- **Purpose**: Real-time paper and trend discovery
- **Triggers**: Step 1 (trends), Step 2 (gap validation)

### Sequential
- **Purpose**: Complex multi-step analysis
- **Triggers**: Step 4 (synthesis), Step 5 (action planning)

---

## Governing Principles

| Principle | Description |
|-----------|-------------|
| Field-Agnostic | Works for any domain |
| Conversational | Dialogue over forms |
| Evidence-Based | Claims require verification |
| Practitioner-First | Real-world applicability |
| Iterative | Context evolves with research |
| Minimum-Viable | Proceed when sufficient, don't over-question |

---

## Examples

See `examples/` for complete research contexts:

- **manufacturing-ai-2026/**: AI adoption for manufacturing practitioners
- **healthcare-scheduling/**: Hospital staff optimization
- **fintech-blockchain/**: Cross-border payments research

Each example includes:
- Research context YAML
- Sample conversation flow
- Expected pipeline outputs

---

## Contributing

Contributions welcome! Areas of interest:
- New domain examples
- Prompt refinements
- Additional language support

---

## License

MIT License - see LICENSE file for details.

---

## Acknowledgments

- Inspired by [plugins-for-claude-natives](https://github.com/team-attention/plugins-for-claude-natives/)
- Design philosophy: Conversational discovery for any domain
