---
name: notebooklm-infographic
description: Use when creating professional infographics automatically using NotebookLM MCP, generating visual content from research topics with automated web search, data structuring, and browser automation for visualization
---

# NotebookLM 인포그래픽 자동 생성

## Overview

NotebookLM MCP를 활용하여 주제에 대한 전문적인 인포그래픽을 완전 자동으로 생성합니다.

**Core capabilities:**
- 🔍 Automated web research and data collection
- 📊 Data structuring and content organization
- 🎨 Automated NotebookLM infographic generation
- 💾 Downloadable image output
- 🌐 Korean/English support

**Total workflow time:** ~5-8 minutes

## When to Use

Use this skill when:
- User requests infographic creation for any topic
- Need to visualize research findings professionally
- Want to combine web research with automated design
- User invokes `/infographic` command or asks for visual content generation

## Prerequisites

Before using this skill, ensure:
- ✅ NotebookLM MCP installed (`claude mcp add notebooklm npx notebooklm-mcp@latest`)
- ✅ Google account logged in to NotebookLM
- ✅ Chrome browser available
- ✅ Internet connection active
- ✅ WebSearch MCP available
- ✅ Browser automation tools loaded (mcp__claude-in-chrome__)

## Workflow Pipeline

### Phase 1: Research & Data Collection (2-3 min)

**Objective:** Gather latest information on the topic

```bash
# Execute web searches
WebSearch(query="{TOPIC} 최신 트렌드 2026")
WebSearch(query="{TOPIC} 통계 데이터")
WebSearch(query="{TOPIC} 전망")
```

**Extract from results:**
- Key statistics (numbers, percentages)
- Trends (growth/decline indicators)
- Sector classifications
- Expert insights

### Phase 2: Content Structuring (1-2 min)

**Structure data using this template:**

```markdown
# {TOPIC}

## 핵심 전망
- **목표/지표**: [숫자]
- **성과**: [통계]
- **추가 여력**: [분석]

## 전략 원칙
1. **원칙1**: 설명
2. **원칙2**: 설명
3. **원칙3**: 설명

## 핵심 섹터/카테고리

### 1순위: [섹터명]
- 성장률: [데이터]
- 포인트: [핵심 내용]

### 2순위: [섹터명]
- 성장률: [데이터]
- 포인트: [핵심 내용]

### 3순위: [섹터명]
- 성장률: [데이터]
- 포인트: [핵심 내용]

## 실행 가이드
- Step 1: [내용]
- Step 2: [내용]
- Step 3: [내용]

## 핵심 용어
- **용어1**: 정의
- **용어2**: 정의

출처: 공개 자료 종합 정리 (날짜)
```

**Save structured content:**
```python
Write(
    file_path="/tmp/claude-{session}/infographic_{topic}.md",
    content=structured_content
)
```

### Phase 3: NotebookLM Notebook Creation (1-2 min)

**Browser preparation:**
```python
# 1. Get browser context
tabs_context_mcp(createIfEmpty=true)

# 2. Navigate to NotebookLM
navigate(tabId=TAB_ID, url="https://notebooklm.google.com")
computer.wait(duration=2)
computer.screenshot()
```

**Create new notebook:**
```python
# 1. Click "새로 만들기" button
computer.left_click(coordinate=[890, 100])

# 2. Enter title
computer.wait(duration=2)
computer.triple_click(coordinate=[168, 31])
computer.type(text="{TOPIC}")
computer.key(text="Return")

# 3. Verify creation
computer.screenshot()
```

**Add source content:**
```python
# 1. Click "소스 추가" button
computer.left_click(coordinate=[184, 148])
computer.wait(duration=1)

# 2. Select "복사한 텍스트"
computer.left_click(coordinate=[761, 645])
computer.wait(duration=1)

# 3. Paste structured content
computer.left_click(coordinate=[589, 512])
computer.type(text=STRUCTURED_CONTENT)

# 4. Click "삽입" button
computer.left_click(coordinate=[758, 678])
computer.wait(duration=3)
```

### Phase 4: Infographic Generation (1-2 min)

**Trigger generation:**
```python
# 1. Find "인포그래픽" button
find(tabId=TAB_ID, query="인포그래픽 button in studio panel")

# 2. Click to generate
computer.left_click(ref="ref_142")  # Use actual ref from find result
computer.wait(duration=3)

# 3. Wait for generation
computer.wait(duration=15)
computer.screenshot()

# 4. Allow additional time if needed
computer.wait(duration=10)
computer.screenshot()
```

**Verify result:**
```python
# 1. Locate generated infographic
find(tabId=TAB_ID, query="{generated_title}")

# 2. Open to view
computer.left_click(ref="ref_182")
computer.wait(duration=2)

# 3. Capture final result
computer.screenshot()
```

### Phase 5: Completion Report

**Report to user:**
```
✅ 인포그래픽 생성 완료!

제목: {생성된 제목}
주요 내용:
- {섹션1}
- {섹션2}
- {섹션3}

다운로드: 화면 우측 상단 다운로드 버튼(↓) 클릭
NotebookLM 노트북: {노트북 URL}
```

## Required Tools Reference

| Tool | Purpose | Phase |
|------|---------|-------|
| `WebSearch` | Information gathering | 1 |
| `Write` | Save structured content | 2 |
| `tabs_context_mcp` | Browser preparation | 3 |
| `navigate` | URL navigation | 3 |
| `computer.screenshot` | Status verification | 3-4 |
| `computer.left_click` | Button interaction | 3-4 |
| `computer.type` | Text input | 3 |
| `computer.wait` | Timing control | 3-4 |
| `find` | Element location | 4 |

## Error Handling

### Browser Connection Failed
```python
try:
    navigate(url="https://notebooklm.google.com")
except:
    tabs_context_mcp(createIfEmpty=true)
    # Retry navigation
```

### Element Not Found
```python
# Fallback: use coordinates
computer.left_click(coordinate=[x, y])
```

### Generation Timeout
```python
# Wait up to 60 seconds
for i in range(4):
    computer.wait(duration=15)
    screenshot = computer.screenshot()
    if "생성 완료" in screenshot:
        break
```

## Infographic Structure

Generated infographics typically include:

- **핵심 전망/목표**: Key goals with statistics
- **전략/원칙**: 3-5 strategic principles
- **핵심 섹터/카테고리**: Ranked categories/sectors
- **실행 가이드**: Step-by-step implementation guide

## Usage Examples

### Example 1: Stock Investment Guide
```
User: /infographic "한국 주식 투자 2026"
Claude: [Executes 5-phase workflow]
Result: Professional infographic with market outlook, strategies, key sectors
```

### Example 2: Technology Trends
```
User: /ig "AI 기술 트렌드" --audience="개발자"
Claude: [Customized for developer audience]
Result: Technical infographic with AI trends and implementation paths
```

### Example 3: Electric Vehicle Market
```
User: /infographic "전기차 시장" --language="en"
Claude: [English language output]
Result: EV market infographic with global statistics
```

## Quality Checklist

Before completing, verify:
- [ ] Topic clearly defined
- [ ] Latest data included (2026)
- [ ] 3-5 core sections structured
- [ ] Visual elements rich (numbers, percentages)
- [ ] Appropriate for target audience
- [ ] Sources cited
- [ ] Downloadable format available

## Optimization Tips

1. **Search efficiency**: Use specific keywords for targeted results
2. **Content length**: 2,000-3,000 words optimal for rich infographics
3. **Structure clarity**: Clear section divisions with headers
4. **Data quality**: Prioritize recent statistics
5. **Visual emphasis**: Highlight numbers and percentages

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Vague search queries | Add year, specific metrics to queries |
| Insufficient wait time | Increase `computer.wait()` durations |
| Coordinates not working | Use `find()` for dynamic element location |
| Content too short | Aim for 2,000+ words with detailed sections |
| Missing sources | Always include citation with date |

## Troubleshooting

### "OPENAI_API_KEY not set"
```bash
export OPENAI_API_KEY=sk-your-key
```

### NotebookLM not loading
- Verify Google account login status
- Check browser automation connection
- Try manual navigation first

### Infographic generation stalled
- Increase wait duration to 30+ seconds
- Check NotebookLM service status
- Verify content meets minimum length requirements

## Real-World Impact

This skill enables:
- **Rapid visualization**: 5-8 minutes vs. hours of manual design
- **Research integration**: Combines web search with visual generation
- **Professional output**: NotebookLM-quality infographics
- **Scalability**: Generate multiple infographics in single session

---

**Skill Type:** Technique (automation workflow)
**Difficulty:** Intermediate (requires browser automation understanding)
**Dependencies:** NotebookLM MCP, WebSearch MCP, Browser automation tools
