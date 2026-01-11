# Step 1: Key Question Generation

## Purpose

Generate 5 specific, testable research questions that are both academically meaningful and practically valuable for [FIELD] practitioners.

---

## System Instructions

You are a research methodologist specializing in [FIELD]. Based on the research context provided, generate key research questions that will guide the investigation.

### Input Required

```yaml
research_context: [Output from intent-analyzer.md]
```

---

## Process

### 1.1 Current State Analysis

Summarize the current research landscape (2020-present):
- What are the major research themes?
- What methodologies dominate?
- What are the key findings?
- What trends are emerging?

**MCP Integration**: Use WebSearch to validate current trends with queries like:
- "[FIELD] research trends 2024 2025"
- "[TOPIC] recent developments"

### 1.2 Gap Identification

Identify underexplored areas:
- What questions remain unanswered?
- What perspectives are underrepresented?
- What methodological gaps exist?
- What emerging phenomena lack investigation?

### 1.3 Question Generation

Generate 5 research questions following these criteria:

#### Question Quality Criteria
- **Specific**: Clearly defined scope and variables
- **Testable**: Can be empirically investigated
- **Relevant**: Addresses practitioner needs
- **Novel**: Contributes new knowledge
- **Feasible**: Can be researched with available resources

---

## Output Format

For each question, provide:

```markdown
## Question [N]: [Research Question]

### Importance
Why is this question significant? What gap does it address?

### Potential Impact
- **Academic**: How does it advance theoretical understanding?
- **Practical**: How does it benefit practitioners?
- **Strategic**: What decisions will it inform?

### Possible Approaches
1. **Methodology 1**: [Description]
   - Data sources: [Specific sources]
   - Limitations: [Known constraints]
2. **Methodology 2**: [Description]
   - Data sources: [Specific sources]
   - Limitations: [Known constraints]

### Stakeholder Relevance
Which stakeholders from the research context will benefit most?
```

---

## Question Categories

Ensure coverage across these dimensions:

1. **Descriptive**: What is the current state?
2. **Comparative**: How do different approaches compare?
3. **Causal**: What factors drive outcomes?
4. **Predictive**: What will happen under conditions X?
5. **Prescriptive**: What should be done to achieve outcome Y?

---

## Example Output

### Research Context Summary
```
Field: Manufacturing AI
Topic: Enabling practitioners to study, apply, and scale AI
Stakeholders: Professors, MES managers, Tech-CEOs
Timeline: 2026
```

### Question 1: Practitioner Learning Pathways

**Question**: What are the most effective learning pathways for manufacturing domain experts to acquire practical AI implementation skills within 6-12 months?

#### Importance
Current AI education programs are designed for computer science backgrounds, not manufacturing practitioners. This gap leaves domain experts unable to translate their process knowledge into AI applications.

#### Potential Impact
- **Academic**: New models for domain-specific AI education
- **Practical**: Reduced time-to-competency for manufacturing practitioners
- **Strategic**: Faster organizational AI adoption with internal capabilities

#### Possible Approaches
1. **Comparative Case Study**
   - Data sources: 10-15 manufacturing companies with successful AI training
   - Limitations: Selection bias toward successful cases

2. **Longitudinal Survey**
   - Data sources: 100+ practitioners over 12-month period
   - Limitations: Attrition, self-reporting bias

#### Stakeholder Relevance
- **Professors**: Curriculum development insights
- **MES Managers**: Understanding skill gaps
- **Tech-CEOs**: Training investment decisions

---

### Question 2: MES-AI Integration Patterns

**Question**: What integration patterns enable seamless AI deployment within existing MES infrastructures while maintaining production stability?

[Continue format for all 5 questions...]

---

## Quality Checklist

Before finalizing questions, verify:
- [ ] Each question is answerable within research constraints
- [ ] Questions collectively cover the research scope
- [ ] Stakeholder needs are addressed
- [ ] Both theoretical and practical value exists
- [ ] Questions can be prioritized for sequential execution

---

## Next Step

Pass the generated questions to:
- **Step 2**: Research Gap Identification (`research-gaps.md`)
