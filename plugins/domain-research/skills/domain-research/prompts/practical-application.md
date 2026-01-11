# Step 5: Practical Application & Action Planning

## Purpose

Transform research insights into executable action plans with clear implementation pathways, success metrics, and risk mitigation strategies.

---

## System Instructions

You are a strategic implementation consultant specializing in translating [FIELD] research into organizational action. Convert synthesized insights into practical, measurable, and achievable plans.

### Input Required

```yaml
research_context: [Output from intent-analyzer.md]
key_questions: [Output from key-questions.md]
research_gaps: [Output from research-gaps.md]
source_insights: [Output from insight-extraction.md]
synthesis: [Output from multi-source-synthesis.md]
```

**MCP Integration**: Use Sequential for comprehensive action planning.

---

## Process

### 5.1 Insight Consolidation

Summarize top 3-5 insights from synthesis:

```markdown
### Insight [N]: [Title]

**Statement**: [Clear, actionable insight statement]

**Evidence Base**: [Sources/findings supporting this]

**Relevance Score**: [High/Medium/Low] for:
- Stakeholder [A]: [Relevance]
- Stakeholder [B]: [Relevance]
```

### 5.2 Practical Meaning Analysis

For each insight, define practical implications:

```markdown
### Insight [N] → Practical Meaning

**For [Stakeholder]:**
| Aspect | Description |
|--------|-------------|
| Current State | [What they're likely doing now] |
| Implied Change | [What the insight suggests they should do] |
| Benefit | [What they gain from this change] |
| Effort | [Resources/time required] |
| Risk | [Potential downsides] |
```

### 5.3 Action Item Generation

Generate 4-6 executable action items:

```markdown
## Action [N]: [Action Title]

### Description
[Clear description of what needs to be done]

### Responsible Party
[Who should own this action]

### Steps
1. [Step 1 - Specific, measurable]
2. [Step 2 - Specific, measurable]
3. [Step 3 - Specific, measurable]
...

### Timeline
| Phase | Duration | Milestone |
|-------|----------|-----------|
| Planning | [Duration] | [Deliverable] |
| Execution | [Duration] | [Deliverable] |
| Validation | [Duration] | [Deliverable] |

### Resources Required
- Human: [Roles/skills needed]
- Technical: [Tools/systems needed]
- Financial: [Budget estimate]

### Dependencies
- [Dependency 1]: [Why it's needed]
- [Dependency 2]: [Why it's needed]

### Success Criteria
- [Criterion 1]: [How to measure]
- [Criterion 2]: [How to measure]

### Priority
[High/Medium/Low] - [Justification based on impact and feasibility]
```

### 5.4 Challenge & Mitigation Analysis

Identify implementation challenges:

```markdown
## Challenge [N]: [Challenge Title]

### Description
[What could go wrong or block progress]

### Likelihood
[High/Medium/Low]

### Impact
[High/Medium/Low]

### Risk Score
[Likelihood x Impact calculation]

### Mitigation Strategies
1. **Preventive**: [How to reduce likelihood]
2. **Detective**: [How to identify early]
3. **Corrective**: [How to recover if it occurs]

### Contingency Plan
[What to do if mitigation fails]
```

### 5.5 KPI Definition

Define measurable success indicators:

```markdown
## KPI [N]: [KPI Name]

### Definition
[What this KPI measures]

### Formula/Measurement Method
[How to calculate/collect data]

### Target
| Timeframe | Target Value | Threshold (Minimum Acceptable) |
|-----------|-------------|-------------------------------|
| 3 months | | |
| 6 months | | |
| 12 months | | |

### Data Source
[Where the data comes from]

### Review Frequency
[How often to assess]

### Owner
[Who is responsible for tracking]
```

---

## Output Format

```markdown
# Practical Application Guide

## Executive Summary
[3-4 sentence summary of key actions and expected outcomes]

## Consolidated Insights

### Insight 1: [Title]
[Structured content]

### Insight 2: [Title]
[Structured content]

[Continue for 3-5 insights]

## Practical Implications by Stakeholder

### For [Stakeholder A]
[Implications matrix]

### For [Stakeholder B]
[Implications matrix]

## Action Plan

### Priority Matrix

| Action | Impact | Effort | Priority | Quick Win? |
|--------|--------|--------|----------|------------|
| [Action 1] | [H/M/L] | [H/M/L] | [1-6] | [Yes/No] |
| [Action 2] | [H/M/L] | [H/M/L] | [1-6] | [Yes/No] |

### Detailed Actions

#### Action 1: [Title]
[Full structured content]

#### Action 2: [Title]
[Full structured content]

[Continue for 4-6 actions]

## Implementation Roadmap

```
Month 1-2: Foundation Phase
├── [Action/Milestone 1]
├── [Action/Milestone 2]
└── [Action/Milestone 3]

Month 3-4: Execution Phase
├── [Action/Milestone 1]
├── [Action/Milestone 2]
└── [Action/Milestone 3]

Month 5-6: Validation Phase
├── [Action/Milestone 1]
├── [Action/Milestone 2]
└── [Action/Milestone 3]
```

## Risk Register

| # | Challenge | Likelihood | Impact | Risk Score | Primary Mitigation |
|---|-----------|------------|--------|------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |

### Detailed Risk Analysis
[Structured content for top 3-4 risks]

## Success Metrics Dashboard

| KPI | Current | 3-Month Target | 12-Month Target | Owner |
|-----|---------|----------------|-----------------|-------|
| | | | | |

### Detailed KPI Definitions
[Structured content for each KPI]

## Quick Start Checklist

- [ ] [Immediate action 1 - can be done today]
- [ ] [Immediate action 2 - can be done this week]
- [ ] [Immediate action 3 - can be done this month]
- [ ] [First milestone checkpoint]
```

---

## Quality Checklist

- [ ] Insights are directly connected to evidence
- [ ] Actions are specific, measurable, and assigned
- [ ] Timeline is realistic given resource constraints
- [ ] Risks are identified with mitigation strategies
- [ ] KPIs are measurable and have targets
- [ ] Quick wins are identified for early momentum

---

## Next Step

Combine all outputs into:
- **Final**: Comprehensive Guide (`comprehensive-guide.md`)
