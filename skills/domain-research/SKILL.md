# Universal Research Framework

## Core Purpose

A domain-agnostic research framework that guides users from **broad exploration to specific domain research** through conversational intent analysis. Works for any field:

- Manufacturing AI → Healthcare AI → FinTech → EdTech → Sustainability → and beyond

### What It Does

1. **Conversational Discovery**: Guide users through natural dialogue to define their research context
2. **Structured Context Building**: Transform vague interests into actionable research parameters
3. **Systematic Research Pipeline**: 5-step process from questions to action plans
4. **Evidence-Based Insights**: Generate findings grounded in research and data
5. **Practical Application**: Convert insights into executable roadmaps

## Target Audience

This framework serves **domain practitioners** across any field:

- **Industry Professionals**: Engineers, managers, analysts seeking evidence-based guidance
- **Academic Researchers**: Faculty, students bridging theory and practice
- **Business Leaders**: Decision-makers needing structured research for strategy
- **Consultants**: Professionals providing research-backed recommendations
- **Policy Makers**: Those needing comprehensive domain understanding

---

## Research Pipeline

### Step 0: Conversational Intent Analysis
**Prompt**: `prompts/intent-analyzer.md`
**Purpose**: Guide users from vague interests to structured research context through dialogue
**Process**:
- Open invitation → Context deepening → Synthesis → Confirmation
- Adaptive questioning based on user type (clear/vague/assigned/exploratory)
**Output**: Structured YAML research context

### Step 1: Key Question Generation
**Prompt**: `prompts/key-questions.md`
**Purpose**: Generate 5 testable, meaningful research questions
**Input**: Research context from Step 0
**Output**: Prioritized questions with importance, impact, and methodology

### Step 2: Research Gap Identification
**Prompt**: `prompts/research-gaps.md`
**Purpose**: Identify underexplored areas and limitations in existing research
**Input**: Key questions from Step 1
**Output**: 4 priority gaps with proposed research ideas

### Step 3: Key Insight Extraction (Single Source)
**Prompt**: `prompts/insight-extraction.md`
**Purpose**: Deep analysis of individual research sources
**Input**: Papers, reports, or documents relevant to the research context
**Output**: Structured findings, implications, limitations

### Step 4: Multi-Source Synthesis
**Prompt**: `prompts/multi-source-synthesis.md`
**Purpose**: Integrate insights across multiple sources
**Input**: Multiple sources + insights from Steps 1-3
**Output**: Common themes, integrated findings, knowledge gaps

### Step 5: Practical Application
**Prompt**: `prompts/practical-application.md`
**Purpose**: Transform insights into executable action plans
**Input**: All previous step outputs
**Output**: Actions, challenges, KPIs, comprehensive roadmap

### Final: Comprehensive Guide
**Prompt**: `prompts/comprehensive-guide.md`
**Purpose**: Single-page practitioner roadmap
**Output**: Scannable guide with findings, timeline, metrics, risks

---

## Example Domains

This framework has been applied to:

| Domain | Example Topic | Stakeholders |
|--------|---------------|--------------|
| Manufacturing AI | AI adoption for SMEs | Engineers, Factory Managers |
| Healthcare AI | Staff scheduling optimization | Hospital Administrators |
| EdTech | AI tutoring implementation | University Faculty |
| FinTech | Blockchain for payments | Strategy Teams |
| Sustainability | Carbon neutrality pathways | Corporate Executives |
| HR Tech | AI in recruitment | HR Directors |
| AgTech | Precision agriculture | Farm Operators |

---

## Governing Principles

```yaml
principles:
  field_agnostic:
    description: "Works for any domain the user brings"
    enforcement: "Dynamic context building, not fixed templates"

  conversational_discovery:
    description: "Natural dialogue over form-filling"
    enforcement: "Adaptive questions based on user clarity level"

  evidence_based:
    description: "All claims require verifiable evidence"
    enforcement: "Citations, data references, empirical validation"

  practitioner_focus:
    description: "Prioritize real-world applicability"
    enforcement: "Each insight maps to concrete action"

  iterative_refinement:
    description: "Context evolves as research progresses"
    enforcement: "Each step builds on previous outputs"

  minimum_viable_context:
    description: "Don't over-question; proceed when sufficient"
    enforcement: "3-6 exchanges typically sufficient for context"
```

---

## MCP Server Integration

### WebSearch Server
- **Trigger**: Step 1 trend analysis, Step 2 gap validation
- **Purpose**: Real-time paper and industry trend discovery
- **Query Pattern**: Dynamic based on research context

### Sequential Server
- **Trigger**: Step 4 synthesis, Step 5 action planning
- **Purpose**: Complex multi-step reasoning and analysis
- **Use Case**: Cross-source synthesis, conflict resolution

---

## Quality Gates

1. **Context Completeness**: All critical fields populated through conversation
2. **Question Testability**: Each question can be empirically investigated
3. **Evidence Strength**: Findings ranked by quality and reliability
4. **Practical Mapping**: Every insight connects to practitioner action
5. **Roadmap Clarity**: Final guide provides clear implementation path

---

## Usage

```bash
# Start research session
claude --skill domain-research

# Begin with conversational discovery
/research

# Or provide initial context
/research "I want to explore AI in healthcare"

# Execute specific steps
/research-questions    # Step 1
/research-gaps         # Step 2
/research-synthesize   # Step 4
/research-action       # Step 5
```

---

## Conversation Examples

### Quick Path (Clear Intent)
```
User: "I want to research AI quality inspection for manufacturing SMEs"
→ 2-3 clarifying questions → Research context generated
```

### Exploratory Path (Vague Intent)
```
User: "I'm curious about AI in my industry"
→ 4-6 discovery questions → Narrowed focus → Research context generated
```

### Assigned Path (External Mandate)
```
User: "My boss wants a report on blockchain"
→ Context questions → Stakeholder alignment → Research context generated
```
