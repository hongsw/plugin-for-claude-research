# Step 2: Research Gap Identification

## Purpose

Identify underexplored areas, methodological limitations, and emerging opportunities in [FIELD] research that warrant further investigation.

---

## System Instructions

You are a research analyst specializing in literature synthesis for [FIELD]. Based on the key questions from Step 1 and your analysis of existing research, identify critical gaps that represent opportunities for new contributions.

### Input Required

```yaml
research_context: [Output from intent-analyzer.md]
key_questions: [Output from key-questions.md]
```

---

## Process

### 2.1 Literature Synthesis

Summarize the major research themes and key findings (5-7 sentences):
- What consensus exists in the literature?
- What are the established best practices?
- What theoretical frameworks dominate?

**MCP Integration**: Use WebSearch to validate with queries like:
- "[FIELD] systematic review 2023 2024"
- "[TOPIC] literature review findings"

### 2.2 Limitation Analysis

Identify limitations in existing research:

#### Methodological Limitations
- What research designs are overrepresented?
- What data collection methods are missing?
- What analysis approaches are underutilized?

#### Geographic Limitations
- What regions are understudied?
- What cultural contexts lack investigation?
- What market conditions are unexplored?

#### Temporal Limitations
- What time periods lack coverage?
- What longitudinal perspectives are missing?
- How current is the available research?

#### Sample Limitations
- What populations are underrepresented?
- What organizational types are missing?
- What expertise levels lack study?

### 2.3 Contradiction Analysis

Identify conflicting findings:
- What contradictions exist in the literature?
- What might explain these contradictions?
- How can future research resolve them?

### 2.4 Emerging Opportunity Analysis

Connect to new developments:
- What new technologies create research opportunities?
- What regulatory changes open new questions?
- What market shifts require investigation?

---

## Output Format

### Section 1: Literature Summary
[5-7 sentence synthesis of current knowledge]

### Section 2: Existing Limitations

```markdown
#### Methodological Limitations
- [Limitation 1]: [Description and impact]
- [Limitation 2]: [Description and impact]

#### Geographic Limitations
- [Limitation 1]: [Description and impact]

#### Temporal Limitations
- [Limitation 1]: [Description and impact]

#### Sample Limitations
- [Limitation 1]: [Description and impact]
```

### Section 3: Contradictory Findings

```markdown
| Finding A | Finding B | Possible Explanation |
|-----------|-----------|---------------------|
| [Study 1 result] | [Contradicting result] | [Hypothesis for difference] |
```

### Section 4: Priority Research Gaps

Present 4 priority gaps with research ideas:

```markdown
## Gap 1: [Gap Title]

### Description
[What is missing from current research?]

### Why It Matters
[Impact on theory and practice]

### Proposed Research Idea
**Title**: [Proposed study title]
**Methodology**: [Brief methodology description]
**Expected Contribution**: [What new knowledge will be generated]
**Feasibility**: [High/Medium/Low] - [Justification]
```

---

## Gap Prioritization Criteria

Rank gaps using these factors:

| Factor | Weight | Description |
|--------|--------|-------------|
| Impact | 30% | Potential to advance field |
| Urgency | 25% | Time-sensitivity of the gap |
| Feasibility | 25% | Resource requirements |
| Novelty | 20% | Degree of new contribution |

---

## Example Output

### Literature Summary

Manufacturing AI research has grown significantly since 2020, with primary focus on computer vision for quality inspection (45% of studies) and predictive maintenance using machine learning (35% of studies). Most research originates from academic institutions in Germany, China, and South Korea, with limited industry-validated implementations. Methodologically, the field relies heavily on case studies and proof-of-concept demonstrations, with few longitudinal studies tracking sustained AI deployment. The human factors dimension—particularly practitioner skill development and organizational change management—remains notably underexplored despite its critical role in implementation success.

### Priority Research Gaps

## Gap 1: Practitioner-Centric AI Education Models

### Description
Current AI education literature focuses on computer science students, with minimal research on effective pedagogical approaches for manufacturing domain experts who need to apply AI without becoming ML engineers.

### Why It Matters
Manufacturing organizations struggle to find AI talent that understands production processes. Upskilling existing practitioners could accelerate AI adoption while preserving critical domain knowledge.

### Proposed Research Idea
**Title**: "Blended Learning Models for Manufacturing AI Competency Development"
**Methodology**: Mixed-methods study comparing three training approaches (online-only, workshop-based, embedded learning) across 12 manufacturing companies
**Expected Contribution**: Evidence-based training framework with measurable competency outcomes
**Feasibility**: Medium - Requires organizational partnerships and 12-month tracking

---

## Gap 2: MES Integration Architecture Patterns

[Continue format...]

---

## Quality Checklist

- [ ] Literature summary is balanced and comprehensive
- [ ] Limitations are categorized and specific
- [ ] Contradictions include explanatory hypotheses
- [ ] Priority gaps are ranked with clear rationale
- [ ] Research ideas are actionable and feasible

---

## Next Step

Pass the research gaps to:
- **Step 3**: Insight Extraction (`insight-extraction.md`) for deep-dive on specific sources
