# Block 0: 환경 설정

## 목표
Claude Code 설치 및 초기 설정을 완료합니다.

## 실행 프로토콜

### Phase A (설명 + 실습 안내)

참조 파일 `references/block0-setup.md`의 EXPLAIN 섹션을 읽고 다음을 설명하세요:

1. **Claude Code 설치 방법**
   - Mac/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows: `irm https://claude.ai/install.ps1 | iex`

2. **설치 확인**
   - 터미널에서 `claude` 명령어 실행
   - 인증 (Anthropic 계정)

3. **초기 설정**
   - 출력 스타일: "Explanatory" 모드 권장 (학습용)
   - 에디터 선택: VS Code, Cursor, Antigravity 중 택 1 (선택사항)

4. **트러블슈팅 안내표**

| 증상 | 해결 |
|------|------|
| Mac 권한 오류 | `sudo` 붙여서 재실행 |
| 설치 후 명령어 인식 안됨 | 터미널 재시작 |
| Windows 실행 정책 | `Set-ExecutionPolicy RemoteSigned` |

참조 파일의 EXECUTE 섹션을 읽고 실습을 안내하세요.

마무리 멘트:
"👆 위 내용을 직접 실행해보세요. 실행이 끝나면 '완료' 또는 '다음'이라고 입력해주세요."

**여기서 STOP. Phase B로 넘어가지 마세요.**

---

### Phase B (확인)

사용자가 "완료" 또는 "다음"이라고 하면:

AskUserQuestion으로 확인:
- "Claude Code가 정상적으로 설치되어 첫 대화를 나눠보셨나요?"
  - 옵션 1: "네, 설치 완료하고 대화도 해봤습니다" ✅
  - 옵션 2: "설치는 했는데 대화는 아직이요"
  - 옵션 3: "설치에 문제가 있습니다"

피드백 후 Block 1로 안내하세요.
