# 기능 3: MCP — 참조 자료

## EXPLAIN

📖 공식 문서: https://code.claude.com/docs/ko/mcp

### MCP란?

MCP (Model Context Protocol) = **Claude와 외부 도구를 연결하는 표준 프로토콜**

### 핵심 개념

```
Claude Code ←→ MCP 프로토콜 ←→ 외부 서비스
                                ├── Slack
                                ├── Calendar
                                ├── Notion
                                ├── GitHub
                                └── 사용자 정의 서비스
```

- Claude는 텍스트 생성뿐 아니라 **도구 호출(Tool Calling)**이 가능
- MCP는 이 도구 호출을 외부 서비스로 확장하는 표준 규격
- 플러그처럼 꽂으면 바로 사용 가능

### 실용적 예시

| MCP 서버 | 할 수 있는 것 |
|----------|-------------|
| Slack MCP | "오늘 온 Slack 메시지 요약해줘" |
| Calendar MCP | "내일 일정 확인해줘" |
| Notion MCP | "회의록 노션에 정리해줘" |
| GitHub MCP | "PR 리뷰 상태 확인해줘" |
| WebSearch MCP | "최신 트렌드 검색해줘" |

### 설정 방법

`.mcp.json` 파일에 서버 정보를 등록:

```json
{
  "mcpServers": {
    "webSearch": {
      "command": "npx",
      "args": ["-y", "@anthropic/web-search-mcp"]
    }
  }
}
```

---

## EXECUTE

1. Claude에게 "MCP를 쉽게 설명해줘"라고 요청해보세요
2. "내 업무에 유용할 MCP 서버 3가지를 추천해줘"라고 물어보세요
3. `.mcp.json` 파일이 있다면 내용을 확인해보세요

---

## QUIZ

- "MCP란 무엇인가요?"
  - 옵션 1: "Claude와 외부 도구를 표준 프로토콜로 연결하는 것" ✅
  - 옵션 2: "Claude의 내장 기능"
  - 옵션 3: "프로그래밍 언어"

→ MCP는 Slack, Calendar 등 외부 서비스를 표준 프로토콜로 Claude에 연결합니다.
