# 기능 5: Agent Teams — 참조 자료

## EXPLAIN

📖 공식 문서: https://code.claude.com/docs/ko/agent-teams

### Agent Teams란?

Agent Teams = **독립적 컨텍스트 창을 가진 에이전트들의 협업 시스템**

### Subagent와의 차이

```
Subagent:
  상사 → 부하 (일방향 위임, 결과만 보고)

Agent Teams:
  에이전트 A ←→ 에이전트 B (상호 소통)
       ↓              ↓
    [공유 작업 목록 (Kanban)]
```

- **Subagent**: 단방향 — 리더에게만 보고
- **Agent Teams**: 양방향 — 에이전트 간 직접 소통 + 공유 작업 목록으로 조율

### 비유

```
Subagent = 상사-부하 관계 (보고만)
Agent Teams = 프로젝트 팀 (소통 + 칸반 보드)
```

### 활성화 방법

`~/.claude/settings.json`에 추가:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

**참고:**
- 실험적 기능입니다
- 분할 화면은 tmux를 사용하며, VS Code 터미널/Windows Terminal/Ghostty에서는 미지원

---

## EXECUTE

1. Claude에게 "Agent Teams 설정을 settings.json에 추가해줘"라고 요청해보세요
2. 설정이 정상 적용되었는지 확인해보세요

---

## QUIZ

- "Agent Teams가 Subagent와 다른 점은?"
  - 옵션 1: "독립 인스턴스 간 직접 소통 + 공유 작업 조율" ✅
  - 옵션 2: "더 빠르게 동작해서"
  - 옵션 3: "별도 설치가 필요해서"

→ Agent Teams는 에이전트 간 양방향 소통과 공유 작업 목록을 통한 협업이 핵심입니다.
