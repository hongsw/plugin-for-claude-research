# Block 5: 스킬 만들기 — 참조 자료

## EXPLAIN

### Skill 만들기 = 마크다운 파일 하나 작성

Skill의 본질은 **마크다운 파일 하나**입니다.
복잡한 코드나 프로그래밍 지식이 필요 없습니다.

### 최소 구성

```
.claude/skills/my-skill/
└── SKILL.md
```

### SKILL.md 작성법

```markdown
---
name: my-skill-name
description: 스킬 설명. "/my-skill-name", "관련 키워드" 요청에 사용.
---

# 스킬 제목

## 이 스킬이 하는 일
- 작업 1
- 작업 2
- 작업 3

## 실행 규칙
1. 첫 번째로 할 것
2. 두 번째로 할 것
3. 마지막으로 할 것
```

### 메타데이터 (Frontmatter)

```yaml
---
name: my-skill          # 스킬 이름 (영문, 하이픈 사용)
description: "설명"      # 자동 매칭에 사용되는 설명
---
```

- `name`: 스킬의 고유 이름
- `description`: Claude가 이 스킬을 언제 사용할지 판단하는 설명

### 실습 예시: morning-routine 스킬

```markdown
---
name: morning-routine
description: 아침 업무 시작 루틴. "/morning-routine", "아침 루틴", "업무 시작" 요청에 사용.
---

# 아침 업무 시작 루틴

사용자가 아침에 업무를 시작할 때 실행하는 스킬입니다.

## 실행 순서

1. **인사**: 오늘 날짜와 요일을 알려주며 인사
2. **일정 확인**: 오늘의 주요 일정이 있는지 물어보기
3. **우선순위 설정**: AskUserQuestion으로 오늘 가장 중요한 업무 3가지 물어보기
4. **할 일 정리**: TodoWrite로 할 일 목록 작성
5. **마무리**: "좋은 하루 되세요!" 메시지와 함께 할 일 요약
```

### 고급: 참조 파일 활용

```
.claude/skills/weekly-report/
├── SKILL.md
└── references/
    ├── report-template.md    # 보고서 템플릿
    └── checklist.md          # 체크리스트
```

SKILL.md에서 참조:
```markdown
## 실행 전 준비
`references/report-template.md`를 읽어서 보고서 형식을 파악합니다.
`references/checklist.md`를 읽어서 누락 사항을 확인합니다.
```

---

## EXECUTE

직접 스킬을 만들어보세요:

1. `.claude/skills/my-first-skill/` 폴더를 만듭니다
2. `SKILL.md` 파일을 작성합니다
3. Claude에게 도움을 요청해도 됩니다: "나만의 morning-routine 스킬을 만들어줘"
4. `/my-first-skill`로 실행하여 확인합니다
5. 결과를 보고 SKILL.md를 수정하며 개선합니다

---

## QUIZ

**확인 질문:**
- "스킬을 만들어보셨나요?"
  - "네, 만들어서 실행까지 해봤습니다" ✅
  - "만들었는데 실행이 안 됩니다"
  - "아직 못 만들었습니다"

**지식 퀴즈:**
- "Skill을 만드는 데 최소한으로 필요한 것은?"
  - "SKILL.md 파일 하나" ✅
  - "복잡한 설정 파일들"
  - "프로그래밍 지식"

→ Skill의 진입 장벽은 마크다운 파일 하나입니다. 누구나 만들 수 있습니다.
