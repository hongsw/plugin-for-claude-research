# Block 3: Claude Code 7대 핵심 기능

## 목표
Claude Code의 7가지 핵심 기능을 하나씩 학습합니다.
각 기능은 독립적인 Phase A → Phase B 사이클을 따릅니다.

## 실행 프로토콜

각 기능별로 해당 참조 파일을 읽고, 아래 순서대로 진행합니다.
사용자가 특정 기능 번호를 지정하면 해당 기능으로 바로 이동합니다.

---

### 기능 1: CLAUDE.md — 영구 기억 장치
**참조**: `references/block3-1-claude-md.md`
📖 공식 문서: https://code.claude.com/docs/ko/memory

**Phase A:**
- CLAUDE.md = 매 대화 시작 시 자동으로 읽히는 시스템 프롬프트
- 팀 위키처럼 규칙과 선호도를 저장
- `/init` → 프로젝트 분석 후 자동 생성
- `/memory` → 패턴/규칙 영구 저장
- 실습: `/init` 또는 `/memory` 실행해보기
- STOP.

**Phase B:**
Quiz: "CLAUDE.md는 언제 읽히나요?"
- "매 대화 시작 시 자동으로" ✅
- "사용자가 수동으로 열 때"
- "하루에 한 번"

---

### 기능 2: Skill — 재사용 레시피
**참조**: `references/block3-2-skill.md`
📖 공식 문서: https://code.claude.com/docs/ko/skills

**Phase A:**
- Skill = 필요할 때만 로드되는 작업 레시피
- CLAUDE.md와의 차이: 항상 로드 vs 호출 시만 로드 (Progressive Loading)
- 최소 구성: SKILL.md 파일 하나
- 실습: 이 학습 스킬 자체가 Skill의 예시
- STOP.

**Phase B:**
Quiz: "Skill이 CLAUDE.md와 다른 핵심 차이는?"
- "필요할 때만 로드되는 Progressive Loading" ✅
- "더 길어서"
- "다른 언어로 작성되어서"

---

### 기능 3: MCP — 외부 도구 연결
**참조**: `references/block3-3-mcp.md`
📖 공식 문서: https://code.claude.com/docs/ko/mcp

**Phase A:**
- MCP = Claude와 외부 도구를 연결하는 표준 프로토콜
- Slack, Calendar, Notion 등 외부 서비스 연동 가능
- Claude에게 "MCP를 쉽게 설명해줘"라고 요청해보기
- STOP.

**Phase B:**
Quiz: "MCP란 무엇인가요?"
- "Claude와 외부 도구를 표준 프로토콜로 연결하는 것" ✅
- "Claude의 내장 기능"
- "프로그래밍 언어"

---

### 기능 4: Subagent — 독립 작업 위임
**참조**: `references/block3-4-subagent.md`
📖 공식 문서: https://code.claude.com/docs/ko/sub-agents

**Phase A:**
- Subagent = 독립된 공간에서 특정 작업을 전담 처리
- 메인 대화의 컨텍스트를 소비하지 않음
- 결과 요약만 메인에 반환
- 실습: 폴더 구조 탐색을 Subagent에 위임해보기
- STOP.

**Phase B:**
Quiz: "Subagent가 중요한 이유는?"
- "별도 처리로 메인 대화 컨텍스트를 절약해서" ✅
- "Claude가 못하는 일을 할 수 있어서"
- "반드시 사용해야 하는 필수 기능이라서"

---

### 기능 5: Agent Teams — 다중 에이전트 협업
**참조**: `references/block3-5-agent-teams.md`
📖 공식 문서: https://code.claude.com/docs/ko/agent-teams

**Phase A:**
- Agent Teams = 독립적 컨텍스트 창을 가진 에이전트들의 협업
- Subagent와의 차이: 에이전트 간 직접 소통 + 공유 작업 목록
- 실험적 기능 — 활성화 필요
- STOP.

**Phase B:**
Quiz: "Agent Teams가 Subagent와 다른 점은?"
- "독립 인스턴스 간 직접 소통 + 공유 작업 조율" ✅
- "더 빠르게 동작해서"
- "별도 설치가 필요해서"

---

### 기능 6: Hook — 이벤트 자동화
**참조**: `references/block3-6-hook.md`
📖 공식 문서: https://code.claude.com/docs/ko/hooks

**Phase A:**
- Hook = 특정 이벤트 발생 시 자동으로 실행되는 셸 스크립트
- AI는 확률적 → Hook은 코드로 결정적 실행
- 예: 응답 완료 시 현재 시간 표시
- 실습: Stop Hook 하나 설정해보기
- STOP.

**Phase B:**
Quiz: "Hook은 언제 실행되나요?"
- "특정 이벤트 발생 시 자동으로" ✅
- "사용자가 수동으로 실행할 때"
- "정해진 시간에 예약 실행"

---

### 기능 7: Plugin — 패키지 배포
**참조**: `references/block3-7-plugin.md`
📖 공식 문서: https://code.claude.com/docs/ko/plugins

**Phase A:**
- Plugin = Skill + MCP + Hook + Agent를 하나의 설치 단위로 묶은 것
- 한 줄로 팀 전체가 동일한 환경 구축
- 이 프로젝트 자체가 Plugin의 예시
- STOP.

**Phase B:**
Quiz: "Plugin이 묶는 것은?"
- "Skill + MCP + Hook + Agent 등을 하나의 패키지로" ✅
- "코드 파일들만"
- "문서 파일들만"

---

### 정리

모든 기능 학습 완료 후:

📖 전체 기능 개요: https://code.claude.com/docs/ko/features-overview

7가지 기능의 관계를 정리:
```
CLAUDE.md (기본 규칙)
  ├── Skill (작업 레시피) ←── MCP (외부 도구)
  ├── Subagent (독립 작업) ←── Agent Teams (협업)
  ├── Hook (이벤트 자동화)
  └── Plugin (통합 배포)
```

"모르면 Claude에게 물어보면 됩니다."

→ Block 4로 이동 안내.
