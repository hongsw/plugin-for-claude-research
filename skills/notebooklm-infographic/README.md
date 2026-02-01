# NotebookLM 인포그래픽 자동 생성 플러그인

NotebookLM MCP를 활용하여 주제에 대한 전문적인 인포그래픽을 완전 자동으로 생성하는 Claude Code 플러그인입니다.

## 🎯 주요 기능

- 🔍 자동 정보 수집 (인터넷 검색)
- 📊 데이터 구조화 및 분석
- 🎨 NotebookLM 자동 인포그래픽 생성
- 💾 다운로드 가능한 이미지 생성
- 🌐 한국어/영어 지원

## 📦 설치 방법

### Claude Code 플러그인으로 설치

```bash
# 마켓플레이스 추가
claude plugin marketplace add https://github.com/hongsw/korea_tech_ai_ppts

# 플러그인 설치
claude plugin install notebooklm-infographic

# 확인
claude plugin list
```

## 🚀 사용 방법

### 기본 사용

```bash
# Claude Code에서
/infographic "주제"
```

### 예시

```bash
# 한국 주식 투자 가이드
/infographic "한국 주식 투자 2026"

# 축약 명령어
/ig "AI 기술 트렌드"

# 옵션 지정
/infographic "전기차 시장" --audience="투자자" --language="ko"
```

## 📋 워크플로우

1. **Phase 1**: 정보 수집 (2-3분)
   - 인터넷 검색으로 최신 정보 수집
   - 데이터 구조화

2. **Phase 2**: NotebookLM 노트북 생성 (1-2분)
   - 웹사이트 접속
   - 노트북 생성 및 데이터 업로드

3. **Phase 3**: 인포그래픽 생성 (1-2분)
   - 자동 인포그래픽 생성
   - 결과 확인

**총 소요 시간**: 약 5-8분

## 🛠️ 사전 요구사항

- ✅ NotebookLM MCP 설치
- ✅ Google 계정 로그인
- ✅ Chrome 브라우저
- ✅ 인터넷 연결

## 📊 생성되는 인포그래픽 구조

- 핵심 전망/목표 (숫자, 통계)
- 전략/원칙 (3-5개)
- 핵심 섹터/카테고리 (순위별)
- 실행 가이드 (단계별)

## 📚 상세 문서

- [사용 설명서](../SKILL_DOCUMENTATION.md)
- [설치 가이드](../PLUGIN_INSTALLATION_GUIDE.md)
- [프로세스 가이드](../notebooklm-infographic-skill.md)

## 🔧 트러블슈팅

### NotebookLM MCP 설치
```bash
claude mcp add notebooklm npx notebooklm-mcp@latest
```

### 브라우저 연결 실패
- Chrome 브라우저 설치 확인
- NotebookLM 로그인 상태 확인

## 📄 라이선스

MIT License

## 👤 작성자

hongsw

## 🙏 감사

- NotebookLM Team (Google)
- Claude Code Team (Anthropic)
- MCP Community

---

**버전**: 1.0.0
**최종 업데이트**: 2026-02-01
