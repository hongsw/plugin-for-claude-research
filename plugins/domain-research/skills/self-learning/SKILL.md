---
name: self-learning
description: Claude Code 자기주도 학습 스킬. "/self-learning", "/learn", "학습", "스킬 배우기" 요청에 사용. ai-native-camp/camp-1 기반의 인터랙티브 학습 프레임워크.
---

# Self-Learning Skill — Claude Code 자기주도 학습

> **Original Work Credit**
> 이 스킬은 [ai-native-camp/camp-1](https://github.com/ai-native-camp/camp-1) 커리큘럼을 기반으로 제작되었습니다.
> 원저작자: **AI Native Camp / Koomook** ([@Koomook](https://github.com/Koomook))

## Core Purpose

사용자가 Claude Code의 핵심 기능을 **스스로 학습**할 수 있도록 돕는 인터랙티브 학습 프레임워크입니다.
[ai-native-camp/camp-1](https://github.com/ai-native-camp/camp-1) 커리큘럼을 기반으로 설계되었습니다.

### 학습 내러티브: 에이전틱 엔지니어 진화

> **교육 방법론: Evolution-Gated Learning (EGL) — 진화 게이트 학습법**
> 실제 프로젝트의 아키텍처 진화를 커리큘럼으로 삼고,
> 각 진화 단계에 강제 게이트(STOP 프로토콜)를 설치하며,
> 도구=교사=학습대상의 재귀적 구조에서 자기주도 학습을 실현합니다.
> **참조**: `references/egl-methodology.md`

이 학습은 마인크래프트 진화 메타포를 활용합니다.
흙집(bash)부터 네더라이트(RAG+메모리)까지, 각 학습 블록은 실제 프로젝트 진화 단계와 대응됩니다.

```
흙집 → 석기 → 청동기 → 철기 → 다이아 → 네더라이트 → 메타
bash   if/else  멀티봇   특화    LLM     RAG+메모리   관찰자
──────────────────────────────────────────────────────────
Block0  Block1-2  Block3   Block3  Block5   Block6     졸업후
설치    체험+이해  에이전트  자동화   스킬제작  리서치결합  플러그인
```

**참조**: `references/evolution-chronicle.md` — 마인크래프트 서버 AI 봇 프로젝트의 실제 진화 사례

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

### Block 0: 🏠 흙집시대 — 환경 설정
**Prompt**: `prompts/setup.md`
**Purpose**: Claude Code 설치 및 초기 설정
**Reference**: `references/block0-setup.md`
**진화 단계**: 인프라가 없으면 아무것도 못 한다 — bash, 설치, 설정

### Block 1: ⛏️ 석기시대 — 체험, 먼저 느껴보기
**Prompt**: `prompts/experience.md`
**Purpose**: Claude Code의 가능성을 데모로 체험 + 에이전틱 진화 개요
**References**:
- `references/block1-experience.md`
- `references/evolution-chronicle.md` — 진화 연대기 사례

### Block 2: 왜 터미널인가?
**Prompt**: `prompts/why-cli.md`
**Purpose**: CLI 기반 Claude Code의 필요성 이해
**Reference**: `references/block2-why.md`

### Block 3: 🗡️ 청동기~철기시대 — 7대 핵심 기능
**Prompt**: `prompts/core-features.md`
**Purpose**: Claude Code 7대 핵심 기능 학습 — 역할 분업, 도메인 특화, 자동화
**References**:
- `references/block3-1-claude-md.md` — CLAUDE.md (시스템 프롬프트)
- `references/block3-2-skill.md` — Skill (재사용 레시피)
- `references/block3-3-mcp.md` — MCP (외부 도구 연결)
- `references/block3-4-subagent.md` — Subagent (독립 작업 위임)
- `references/block3-5-agent-teams.md` — Agent Teams (다중 에이전트 협업)
- `references/block3-6-hook.md` — Hook (이벤트 자동화)
- `references/block3-7-plugin.md` — Plugin (패키지 배포)
- `references/evolution-chronicle.md` — 각 기능과 진화 시대의 매핑

### Block 4: 기초 다지기
**Prompt**: `prompts/basics.md`
**Purpose**: CLI, Git, GitHub, 에디터 기초
**Reference**: `references/block4-basics.md`

### Block 5: 💎 다이아몬드시대 — 스킬 만들기 실습
**Prompt**: `prompts/create-skill.md`
**Purpose**: 직접 Skill을 만들어보는 실습 — LLM에게 프롬프트로 행동을 지시하는 단계
**Reference**: `references/block5-create-skill.md`

### Block 6: 🟣 네더라이트시대 — 리서치와 학습의 결합
**Prompt**: `prompts/research-integration.md`
**Purpose**: RAG 기반 지식 외부화 + 학습 — domain-research 스킬과 결합
**References**:
- `references/block6-research-integration.md`
- `references/evolution-chronicle.md` — 네더라이트시대 RAG 패턴과 졸업 후 전망

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

## 학습 완료 후 — 메타시대로

학습을 마친 사용자는 네더라이트시대를 넘어 **메타시대**에 진입합니다:

1. Claude Code의 7대 핵심 기능을 이해 (청동기~철기)
2. 직접 Skill을 만들 수 있는 능력 보유 (다이아몬드)
3. RAG와 리서치를 활용한 지식 외부화 (네더라이트)
4. Plugin 배포 + 시스템 관찰/자동화 (메타)

### 에이전틱 엔지니어 진화 완료 체크

```
🏠 흙집      → Block 0: 환경 설정 완료
⛏️ 석기      → Block 1-2: 체험 + CLI 이해
🗡️ 청동기    → Block 3: 에이전트 분업 (Subagent, Agent Teams)
⚔️ 철기      → Block 3: 도메인 특화 (Hook, MCP)
💎 다이아    → Block 5: LLM 기반 Skill 제작
🟣 네더라이트 → Block 6: RAG + 리서치 결합
🌐 메타      → 졸업 후: Plugin 배포, 팀 공유, 시스템 관찰
```

---

## 연계 스킬

- **domain-research**: 학습 후 실제 리서치 프로젝트에 적용 (네더라이트시대)
- **create-skill** (Block 5): 나만의 스킬 제작 실습 (다이아몬드시대)
