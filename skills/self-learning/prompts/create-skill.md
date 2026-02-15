# Block 5: 스킬 만들기 실습

## 목표
직접 Skill을 만들어보면서 스킬 시스템을 체득합니다.

## 실행 프로토콜

### Phase A (설명 + 실습)

참조 파일 `references/block5-create-skill.md`를 읽으세요.

#### Skill의 최소 구성

```
.claude/skills/my-skill/
└── SKILL.md
```

SKILL.md 하나만 있으면 Skill입니다. 이 파일이 곧 레시피입니다.

#### SKILL.md 기본 구조

```markdown
---
name: my-skill
description: 나의 첫 번째 스킬. "/my-skill" 요청에 사용.
---

# 나의 첫 번째 스킬

이 메시지가 보이면 스킬이 정상 동작하는 것입니다!

## 실행 내용
- 사용자에게 인사
- 현재 날짜와 시간 알려주기
- 오늘의 할 일 물어보기
```

#### 실습: 나만의 스킬 만들기

다음 단계를 따라 직접 스킬을 만들어보세요:

1. **스킬 폴더 생성**
   ```bash
   mkdir -p .claude/skills/my-first-skill
   ```

2. **SKILL.md 작성**
   - Claude에게 요청: "나만의 스킬을 만들고 싶어. 매일 아침 업무 시작할 때 쓸 수 있는 morning-routine 스킬을 만들어줘"

3. **스킬 실행**
   - `/my-first-skill` 입력하여 실행 확인

4. **개선**
   - 실행 결과를 보고 SKILL.md를 수정하며 개선

#### 고급: 참조 파일 추가

```
.claude/skills/my-skill/
├── SKILL.md
└── references/
    └── checklist.md    # 참조 데이터
```

SKILL.md에서 `references/checklist.md`를 읽도록 지시하면, 더 복잡한 스킬도 가능합니다.

마무리 멘트:
"👆 위 내용을 직접 실행해보세요. 나만의 스킬을 하나 만들어보세요! 완료되면 '완료' 또는 '다음'이라고 입력해주세요."

**여기서 STOP.**

---

### Phase B (검증 + 피드백)

AskUserQuestion으로 확인:

"스킬을 만들어보셨나요?"
- "네, 만들어서 실행까지 해봤습니다" ✅
- "만들었는데 실행이 안 됩니다"
- "아직 못 만들었습니다"

옵션별 피드백:
- 성공: 축하 + 스킬 구조의 핵심 복습 (SKILL.md = 레시피)
- 실행 안됨: 경로 확인 (.claude/skills/ 하위), SKILL.md 파일명 확인, description 필드 확인
- 미시도: 가장 간단한 예시 제공하고 재도전 격려

Quiz (AskUserQuestion):
"Skill을 만드는 데 최소한으로 필요한 것은?"
- "SKILL.md 파일 하나" ✅
- "복잡한 설정 파일들"
- "프로그래밍 지식"

→ Block 6으로 이동 안내.
