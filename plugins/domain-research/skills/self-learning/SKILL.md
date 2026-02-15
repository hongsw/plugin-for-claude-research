---
name: self-learning
description: Claude Code 자기주도 학습 스킬. "/self-learning", "/learn", "학습", "스킬 배우기" 요청에 사용. ai-native-camp/camp-1 기반의 인터랙티브 학습 프레임워크.
---

# Self-Learning Skill — Claude Code 자기주도 학습

## Core Purpose

사용자가 Claude Code의 핵심 기능을 **스스로 학습**할 수 있도록 돕는 인터랙티브 학습 프레임워크입니다.
[ai-native-camp/camp-1](https://github.com/ai-native-camp/camp-1) 커리큘럼을 기반으로 설계되었습니다.

### 학습 방식: STOP 프로토콜

각 블록은 반드시 **2턴 구조**를 따릅니다:

**Phase A (1턴)**: 개념 설명 → 실습 지시 → **STOP** (퀴즈 없음, 질문 없음)
- 참조 문서의 EXPLAIN 섹션을 읽고 설명
- 참조 문서의 EXECUTE 섹션을 읽고 실습 안내
- 마무리: "👆 위 내용을 직접 실행해보세요. 실행이 끝나면 '완료' 또는 '다음'이라고 입력해주세요."

**Phase B (2턴)**: 퀴즈 → 피드백 → 다음 블록 안내
- 참조 문서의 QUIZ 섹션을 읽고 AskUserQuestion으로 퀴즈 출제
- 정답/오답 피드백 제공
- 다음 블록으로 이동 여부 확인

### 절대 규칙
1. Phase A에서 절대 AskUserQuestion을 호출하지 않는다
2. Phase A에서 퀴즈 내용을 절대 노출하지 않는다
3. "해보셨나요?" 같은 질문을 하지 않는다
4. 각 블록 시작 전 공식 문서 URL을 출력한다

---

## 학습 과정 (Learning Pipeline)

### Block 0: 환경 설정
**Prompt**: `prompts/setup.md`
**Purpose**: Claude Code 설치 및 초기 설정
**Reference**: `references/block0-setup.md`

### Block 1: 체험 — 먼저 느껴보기
**Prompt**: `prompts/experience.md`
**Purpose**: Claude Code의 가능성을 3가지 데모로 체험
**Reference**: `references/block1-experience.md`

### Block 2: 왜 터미널인가?
**Prompt**: `prompts/why-cli.md`
**Purpose**: CLI 기반 Claude Code의 필요성 이해
**Reference**: `references/block2-why.md`

### Block 3: 7대 핵심 기능
**Prompt**: `prompts/core-features.md`
**Purpose**: Claude Code 7대 핵심 기능 학습
**References**:
- `references/block3-1-claude-md.md` — CLAUDE.md (시스템 프롬프트)
- `references/block3-2-skill.md` — Skill (재사용 레시피)
- `references/block3-3-mcp.md` — MCP (외부 도구 연결)
- `references/block3-4-subagent.md` — Subagent (독립 작업 위임)
- `references/block3-5-agent-teams.md` — Agent Teams (다중 에이전트 협업)
- `references/block3-6-hook.md` — Hook (이벤트 자동화)
- `references/block3-7-plugin.md` — Plugin (패키지 배포)

### Block 4: 기초 다지기
**Prompt**: `prompts/basics.md`
**Purpose**: CLI, Git, GitHub, 에디터 기초
**Reference**: `references/block4-basics.md`

### Block 5: 스킬 만들기 실습
**Prompt**: `prompts/create-skill.md`
**Purpose**: 직접 Skill을 만들어보는 실습
**Reference**: `references/block5-create-skill.md`

### Block 6: 리서치와 학습의 결합
**Prompt**: `prompts/research-integration.md`
**Purpose**: domain-research 스킬과 학습 결합 활용법
**Reference**: `references/block6-research-integration.md`

---

## 네비게이션

사용자가 학습을 시작하면:
1. 현재 수준을 파악 (초보/중급/고급)
2. 적절한 블록부터 시작 제안
3. 블록 번호 또는 "다음"/"이전"/"건너뛰기"로 이동

### 시작 명령어
```
/self-learning          # 처음부터 시작
/learn block3           # 특정 블록으로 이동
/learn skill            # 스킬 만들기 실습
/learn research         # 리서치 결합 학습
```

---

## 학습 완료 후

학습을 마친 사용자는:
1. Claude Code의 7대 핵심 기능을 이해
2. 직접 Skill을 만들 수 있는 능력 보유
3. domain-research 스킬을 활용한 심화 학습 가능
4. MCP 서버 연동을 통한 외부 도구 활용 가능

---

## 연계 스킬

- **domain-research**: 학습 후 실제 리서치 프로젝트에 적용
- **create-skill** (Block 5): 나만의 스킬 제작 실습
