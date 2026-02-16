# 에이전틱 엔지니어 진화 연대기 — 마인크래프트 케이스 스터디

> 마인크래프트에서 플레이어가 석기시대 → 철기시대 → 다이아 시대로 성장하듯이,
> 코딩 아키텍처도 **조건문 → 역할 분업 → LLM → 멀티에이전트 → RAG+LLM**으로 진화한다.

---

## EXPLAIN

### 왜 이 사례를 배우는가?

이 연대기는 실제 프로젝트(마인크래프트 서버 AI 봇)가 2주 만에 거친 진화를 보여줍니다.
각 시대는 Claude Code 학습 블록과 정확히 대응됩니다:

```
학습 블록          마인크래프트 시대           핵심 패턴
─────────────────────────────────────────────────────────
Block 0 (설치)  ←→  흙집시대 (bash)          절차적 스크립트
Block 1 (체험)  ←→  석기시대 (if/else)       조건문 코딩
Block 3 (기능)  ←→  청동기~철기 (역할/상태)  멀티에이전트, 도메인 특화
Block 5 (스킬)  ←→  다이아시대 (LLM)         AI 판단 + 자동화
Block 6 (리서치) ←→ 네더라이트 (RAG+메모리)   지식 외부화 + 학습
```

### 목표

이 케이스 스터디를 통해:
1. **코딩 아키텍처가 어떻게 진화하는지** 큰 그림을 이해
2. **각 Claude Code 기능이 어떤 진화 단계에 해당하는지** 실감
3. **자신의 프로젝트에서 같은 진화를 주도**할 수 있는 관점 획득

---

## 6개 시대 + 메타시대

### 시대 1: 흙집시대 — 서버 설치와 bash 스크립트

> **대표 파일**: `start.sh`, `stop.sh`, 서버 설정 파일

```
기술: bash 스크립트, Java 설정, EULA
지능: 없음 (수동 조작)
패턴: 절차적 스크립트
```

- Minecraft Paper 1.21.11 서버 설치
- Java 8 → Java 17 업그레이드 (호환성 문제 해결)
- Geyser 플러그인으로 Bedrock/Java 크로스플랫폼

> **핵심 교훈**: 인프라가 없으면 아무것도 못 한다
> → Claude Code **Block 0 (환경 설정)**과 대응

---

### 시대 2: 석기시대 — 하드코딩 단일 봇

> **대표 파일**: `simple_agent.js` (164줄), `claude_agent_example.js` (241줄)

```
기술: mineflayer API, if/else 분기
지능: 없음 (정해진 규칙만)
패턴: 이벤트 핸들러 + 조건문
```

```javascript
// 이 시대의 전형적 코드
if (msg.includes('follow')) bot.pathfinder.follow(player);
else if (msg.includes('come')) bot.pathfinder.goto(player.position);
else if (msg.includes('jump')) bot.setControlState('jump', true);
```

- 단일 봇 "ClaudeBot" — 10개 명령어
- 이벤트 기반: 채팅 → 조건 분기 → 액션
- 클래스 구조로 재사용성 확보

> **핵심 교훈**: 명령어마다 코드 추가 = 확장 한계
> → Claude Code **Block 1 (체험)**에서 "이건 AI 없이는 힘들다"를 느끼는 순간

---

### 시대 3: 청동기시대 — 멀티에이전트 팀 시스템

> **대표 파일**: `multi_agent.js` (302줄), `agent_controller.js` (177줄)

```
기술: 역할 기반 분업, 중앙 통제
지능: 없음 (역할별 하드코딩)
패턴: Factory + Command + Observer
```

```javascript
// 이 시대의 혁신: 역할 분화
const roles = {
  Builder:  { task: 'construction', spawn: {...} },
  Guard:    { task: 'security',     spawn: {...} },
  Miner:    { task: 'mining',       spawn: {...} },
  Farmer:   { task: 'agriculture',  spawn: {...} },
  Helper:   { task: 'support',      spawn: {...} },
};
```

- 5봇 팀: Builder, Guard, Miner, Farmer, Helper
- 중앙 통제: "모두 집합", "모두 멈춰"
- AgentManager 클래스로 봇 생성/제거 API화
- REPL 인터페이스로 실시간 제어

> **핵심 교훈**: 분업은 강력하지만, 각 봇은 여전히 멍청하다
> → Claude Code **Block 3 (Subagent, Agent Teams)**에서 배우는 에이전트 분업과 동일

---

### 시대 4: 철기시대 — 전투 특화와 안정화

> **대표 파일**: `guardian_team.js` (374줄), `stable_guardian_team.js` (243줄)

```
기술: PvP 플러그인, 상태 머신, 안정화
지능: 규칙 기반 (위협 감지 → 반응)
패턴: State Machine + Strategy
```

```javascript
// 이 시대의 혁신: 상태 기반 행동
if (threat.name === 'creeper') flee(threat);
else if (role === 'tank') engageFront(threat);
else if (role === 'ranger') keepDistance(threat);
// + 스팸 방지, 쿨다운, 주기적 상태 보고
```

- 전투 역할: Tank, DPS, Healer, Ranger, Scout
- mineflayer-pvp, mineflayer-armor-manager 도입
- stable 버전: 채팅 쿨다운(3초), 5초마다 위협 스캔

> **핵심 교훈**: 도메인 특화 = 품질 향상, 프로덕션 = 안정성 우선
> → Claude Code **Block 3 (Hook, MCP)**에서 배우는 도메인 특화 자동화와 동일

---

### 시대 5: 다이아몬드시대 — LLM 통합 서바이벌 AI

> **대표 파일**: `companion_bot.js` (1,978줄), `fading_assistant.js` (518줄)

```
기술: Ollama(qwen3:32b), 자연어 이해, 목표 분해
지능: LLM 기반 판단 (채팅 → JSON → 액션)
패턴: LLM Router + Goal Decomposition + State Machine
```

```javascript
// 이 시대의 혁신: LLM이 판단한다
const cmd = await askLLM(playerMessage, context);
// → {"action":"craft", "item":"stone_pickaxe", "goal":"iron_pickaxe"}

// 복합 목표 자동 분해
"철곡괭이 만들어줘" → [
  chop → craft planks → craft sticks → craft crafting_table →
  craft wooden_pickaxe → mine cobblestone → craft stone_pickaxe →
  mine iron_ore → craft furnace → smelt iron_ingot → craft iron_pickaxe
]
```

- LLM이 한국어 채팅을 JSON으로 변환
- 복합 목표 루프: LLM이 "다음 한 단계"를 반복 결정
- 낮/밤 인식, 안전 판단, 자동 대피
- 실제 월드 조작: 건축, 채굴, 제련, 제작

> **핵심 교훈**: LLM = 만능 파서, 하지만 느리고(15-30초) 때로 환각
> → Claude Code **Block 5 (스킬 만들기)**에서 AI에게 복잡한 작업을 프롬프트로 지시하는 것과 동일

---

### 시대 6: 네더라이트시대 — RAG + 경험 메모리

> **대표 파일**: `companion_bot.js` + `knowledge.json` (421줄) + `memory.jsonl`

```
기술: RAG(지식 검색), 영속 메모리, 동적 프롬프트
지능: 경험 학습 (과거 성공/실패 참조)
패턴: RAG + Memory Persistence + Hybrid (하드코딩+동적)
```

```javascript
// 이 시대의 혁신: 외부 지식 + 경험 기억
const knowledge = getRelevantKnowledge(message);  // knowledge.json에서 관련 정보만
const experience = getRecentExperience();          // memory.jsonl에서 최근 5개
const context = getBotContext();                    // 인벤, 주변, 시간, 체력
systemPrompt += `\n📖 RAG 지식:\n${knowledge}`;   // LLM에 주입
```

- `knowledge.json`: 레시피 31개, 제련 9개, 아이템 52개, 블록 16개
- `memory.jsonl`: 모든 행동을 `{time, action, item, result, note}`로 영속 기록
- 선택적 지식 주입: 메시지에 "철" → 제련 정보만 로드 (토큰 절약)
- 재시작해도 과거 경험 20개 자동 로드

> **핵심 교훈**: 지식 외부화 = 코드 수정 없이 확장, 메모리 = 학습하는 봇
> → Claude Code **Block 6 (리서치 결합)**에서 배우는 RAG 기반 지식 통합과 동일

---

### 메타시대: 관찰자 계층 — 크로니클과 모니터링

> **대표 파일**: `daily_chronicle.js` (326줄), `manga_chronicle.js` (238줄), `monitor_agents.js` (176줄)

```
기술: Observer 패턴, 서사 생성, 실시간 대시보드
지능: 메타 인식 (봇이 봇을 관찰)
패턴: Observer + Narrative Generator
```

- 봇 활동을 만화/연대기 형태로 자동 기록
- 11개 캐릭터 성격 프로필
- 실시간 위치/체력/활동 모니터링
- `chronicles/` 디렉토리에 에피소드 저장

> **핵심 교훈**: 메타 레이어는 디버깅이자 엔터테인먼트
> → Claude Code의 **Hook + Agent Teams**를 결합한 관찰/자동화 시스템

---

## 진화 비교표

| 시대 | 대표 파일 | 줄수 | AI | 멀티 | 전투 | 건축 | 메모리 | RAG |
|------|----------|------|-----|------|------|------|--------|-----|
| 흙집 | start.sh | ~20 | - | - | - | - | - | - |
| 석기 | simple_agent.js | 164 | - | - | - | - | - | - |
| 청동기 | multi_agent.js | 302 | - | 5봇 | - | - | - | - |
| 철기 | guardian_team.js | 374 | - | 5봇 | PvP | - | - | - |
| 다이아 | companion_bot.js | ~1,750 | LLM | - | O | O | 인메모리 | - |
| 네더라이트 | +knowledge/memory | ~1,978 | LLM | - | O | O | 영속 | O |
| 메타 | chronicle/monitor | ~740 | - | - | - | - | - | - |

---

## 핵심 패턴 진화

```
[조건문]         →  [역할 분업]       →  [LLM 판단]        →  [RAG+메모리]
if/else            Factory/Role         askLLM()+JSON        knowledge.json
정적, 빠름         정적, 확장가능        동적, 느림            동적, 학습
명령어=코드         역할=코드            프롬프트=행동          파일=지식
```

---

## Claude Code 학습과의 매핑

이 진화를 **Claude Code로 재현**하면:

| 마인크래프트 시대 | Claude Code 대응 | 핵심 기능 |
|-----------------|-----------------|----------|
| 흙집 (bash) | Block 0: 환경 설정 | 터미널, 설치 |
| 석기 (if/else) | Block 1-2: 체험 + 이해 | CLI 기초 |
| 청동기 (멀티에이전트) | Block 3: Subagent, Agent Teams | 에이전트 분업 |
| 철기 (도메인 특화) | Block 3: Hook, MCP | 이벤트 자동화, 외부 연결 |
| 다이아 (LLM) | Block 5: Skill 제작 | 프롬프트 = 행동 |
| 네더라이트 (RAG) | Block 6: 리서치 결합 | 지식 외부화 + 학습 |
| 메타 (관찰자) | 졸업 후: Plugin 배포 | 시스템 관찰 + 공유 |

---

## 당신의 진화는?

이 학습을 마치면, 당신도 같은 진화를 경험하게 됩니다:

1. **흙집**: Claude Code를 설치한다 (Block 0)
2. **석기**: 명령어를 하나씩 직접 입력한다 (Block 1-2)
3. **청동기**: Subagent에게 작업을 위임한다 (Block 3)
4. **철기**: Hook과 MCP로 자동화한다 (Block 3)
5. **다이아**: Skill을 만들어 복잡한 작업을 프롬프트로 해결한다 (Block 5)
6. **네더라이트**: RAG와 리서치로 지식을 외부화하고 학습한다 (Block 6)
7. **메타**: Plugin으로 팀과 공유하고, 시스템 전체를 관찰한다 (졸업 후)

> 흙집에서 네더라이트까지, 이 학습이 당신의 에이전틱 엔지니어 진화를 안내합니다.

---

## EXECUTE

1. 위의 진화 비교표를 읽고, 자신이 현재 어느 시대에 있는지 생각해보세요
2. Claude Code 학습과의 매핑을 보고, 어느 블록이 자신에게 가장 필요한지 판단해보세요
3. 준비가 되면 Block 0부터 시작하거나, 필요한 블록으로 바로 이동하세요

---

## QUIZ

"이 진화 연대기에서 가장 큰 전환점은?"
- 옵션 1: "if/else에서 역할 분업으로 (구조화)"
- 옵션 2: "하드코딩에서 LLM으로 (지능 추가)"
- 옵션 3: "LLM에서 RAG+메모리로 (학습 능력)"

→ 정답 없음. 각 전환점의 의미를 설명하고, 자신의 프로젝트에서 어떤 전환이 필요한지 생각하도록 안내.
