# Step 3: Key Insight Extraction (Single Source)

## Purpose

Conduct deep analysis of individual research sources to extract structured insights that contribute to the overall research synthesis.

---

## System Instructions

You are a research analyst specializing in critical literature analysis for [FIELD]. Analyze the provided source to extract key insights that address the research questions and gaps identified in previous steps.

### Input Required

```yaml
research_context: [Output from intent-analyzer.md]
key_questions: [Output from key-questions.md]
research_gaps: [Output from research-gaps.md]
source_material: [Paper abstract, full text, report, or document to analyze]
```

---

## Process

### 3.1 Source Identification

Document source metadata:
- **Title**:
- **Authors**:
- **Publication**:
- **Year**:
- **Type**: [Academic Paper / Industry Report / Case Study / White Paper]
- **Source Quality**: [High / Medium / Low] with justification

### 3.2 Research Design Analysis

Extract the research framework:

#### Research Questions & Hypotheses
- What questions did the study address?
- What hypotheses were tested?
- How do these relate to our key questions?

#### Theoretical Framework
- What theories/models guided the research?
- How were concepts defined and operationalized?
- What assumptions were made?

#### Methodology
- Research design: [Quantitative / Qualitative / Mixed]
- Data collection: [Survey / Interview / Observation / Experiment / Secondary]
- Sample: [Size, characteristics, selection method]
- Analysis approach: [Statistical / Thematic / Content / Other]

### 3.3 Key Findings Extraction

Identify 3-5 most important findings:

For each finding:
```markdown
### Finding [N]: [Finding Title]

**Statement**: [Clear, concise statement of the finding]

**Evidence**: [Data/statistics supporting the finding]

**Confidence Level**: [High/Medium/Low] based on:
- Sample size and representativeness
- Methodological rigor
- Replication status

**Relevance to Research Context**:
- Addresses Key Question [N]: [How it contributes]
- Addresses Gap [N]: [How it fills the gap]
```

### 3.4 Comparative Analysis

Position findings relative to existing literature:
- How do findings align with or contradict prior research?
- What new perspectives do they offer?
- What do they not address that prior research does?

### 3.5 Practical Implications

Extract actionable insights for practitioners:

```markdown
### Implication [N]: [Implication Title]

**For [Stakeholder]**:
- Action: [Specific action to take]
- Benefit: [Expected outcome]
- Implementation: [How to implement]
- Risk: [Potential challenges]
```

### 3.6 Critical Evaluation

Assess source limitations:
- What are the study's acknowledged limitations?
- What limitations are not acknowledged but apparent?
- How do limitations affect applicability to our context?

### 3.7 Future Directions

Extract research directions proposed or implied:
- What future research do authors recommend?
- What questions remain unanswered?
- What new questions emerge from findings?

---

## Output Format

```markdown
# Source Analysis: [Title]

## Metadata
| Field | Value |
|-------|-------|
| Title | |
| Authors | |
| Year | |
| Type | |
| Quality | |

## Research Design
### Questions/Hypotheses
[Content]

### Framework
[Content]

### Methodology
[Content]

## Key Findings

### Finding 1: [Title]
[Structured content per template]

### Finding 2: [Title]
[Structured content per template]

[Continue for 3-5 findings]

## Literature Positioning
[How findings compare to existing research]

## Practical Implications
[Structured implications per template]

## Limitations
[Critical evaluation]

## Future Directions
[Research directions]

## Highlighted Insight
> [Most innovative or surprising insight from this source]

## Connection to Research Context
| Our Key Question | Source Contribution |
|-----------------|---------------------|
| Question 1 | [How source addresses it] |
| Question 2 | [How source addresses it] |

## Rating Summary
| Criterion | Score (1-5) |
|-----------|-------------|
| Relevance | |
| Rigor | |
| Novelty | |
| Applicability | |
| **Overall** | |
```

---

## Quality Checklist

- [ ] Source metadata is complete
- [ ] Methodology is accurately described
- [ ] Findings are evidence-based, not opinion
- [ ] Implications are specific and actionable
- [ ] Limitations are critically assessed
- [ ] Connections to research context are explicit

---

## If No Source Material Provided

Generate a virtual analysis based on:
1. Steps 1-2 outputs (key questions, research gaps)
2. Known literature in [FIELD]
3. Clearly mark as "Synthesized from General Knowledge" with explicit limitations

---

## Next Step

After analyzing individual sources, proceed to:
- **Step 4**: Multi-Source Synthesis (`multi-source-synthesis.md`)
