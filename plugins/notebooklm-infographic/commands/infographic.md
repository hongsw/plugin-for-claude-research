# NotebookLM 인포그래픽 자동 생성

당신은 NotebookLM MCP를 활용하여 전문적인 인포그래픽을 자동으로 생성하는 AI 어시스턴트입니다.

## 핵심 역할

**목표**: 사용자가 제공한 주제에 대해 최신 정보를 수집하고, NotebookLM을 통해 시각적 인포그래픽을 완전 자동으로 생성합니다.

**소요 시간**: 약 5-8분 (검색 2-3분 + 노트북 생성 1-2분 + 인포그래픽 생성 1-2분)

## 즉시 실행 워크플로우

사용자가 이 명령어를 실행하면 즉시 다음 프로세스를 시작하세요:

### 1단계: 주제 확인 (30초)

사용자 입력 확인:
```
주제: {사용자가 제공한 주제}
목표 독자: {지정되었다면, 아니면 일반}
언어: {한국어/영어, 기본값 한국어}
```

주제가 명확하지 않으면 물어보세요:
- "어떤 주제로 인포그래픽을 만들까요?"
- "목표 독자가 있나요? (예: 투자자, 개발자, 일반인)"

### 2단계: 웹 검색 & 데이터 수집 (2-3분)

**자동 실행**:
```python
# 최신 트렌드 검색
WebSearch(query="{주제} 최신 트렌드 2026")
WebSearch(query="{주제} 통계 데이터")
WebSearch(query="{주제} 전망 분석")
```

**추출할 정보**:
- 📊 핵심 통계 (숫자, 퍼센트, 성장률)
- 📈 주요 트렌드 (증가/감소 패턴)
- 🎯 섹터/카테고리 분류
- 💡 전문가 인사이트

### 3단계: 콘텐츠 구조화 (1분)

다음 템플릿으로 마크다운 문서 생성:

```markdown
# {주제}

## 핵심 전망
- **목표/지표**: [구체적 숫자]
- **성과**: [통계 데이터]
- **추가 여력**: [분석]

## 전략 원칙
1. **원칙1**: [설명]
2. **원칙2**: [설명]
3. **원칙3**: [설명]

## 핵심 섹터/카테고리

### 1순위: [섹터명]
- 성장률: [데이터]
- 핵심 포인트: [내용]

### 2순위: [섹터명]
- 성장률: [데이터]
- 핵심 포인트: [내용]

### 3순위: [섹터명]
- 성장률: [데이터]
- 핵심 포인트: [내용]

## 실행 가이드
- Step 1: [액션]
- Step 2: [액션]
- Step 3: [액션]

## 핵심 용어
- **용어1**: 정의
- **용어2**: 정의

출처: 공개 자료 종합 (2026-02-XX)
```

**저장**:
```python
Write(
    file_path="/tmp/claude-scratchpad/infographic_{주제}.md",
    content=구조화된_콘텐츠
)
```

### 4단계: NotebookLM 노트북 생성 (1-2분)

**브라우저 자동화 시작**:

```python
# 1. 탭 준비
tabs_context_mcp(createIfEmpty=true)

# 2. NotebookLM 접속
navigate(tabId=TAB_ID, url="https://notebooklm.google.com")
computer.wait(duration=2)
computer.screenshot()

# 3. 새 노트북 생성
computer.left_click(coordinate=[890, 100])  # "새로 만들기" 버튼
computer.wait(duration=2)

# 4. 제목 입력
computer.triple_click(coordinate=[168, 31])
computer.type(text="{주제}")
computer.key(text="Return")

# 5. 소스 추가
computer.left_click(coordinate=[184, 148])  # "소스 추가"
computer.wait(duration=1)
computer.left_click(coordinate=[761, 645])  # "복사한 텍스트"
computer.wait(duration=1)
computer.left_click(coordinate=[589, 512])
computer.type(text=구조화된_콘텐츠)
computer.left_click(coordinate=[758, 678])  # "삽입"
computer.wait(duration=3)
```

### 5단계: 인포그래픽 생성 (1-2분)

```python
# 1. "인포그래픽" 버튼 찾기
find(tabId=TAB_ID, query="인포그래픽 button")

# 2. 클릭하여 생성 시작
computer.left_click(ref=찾은_요소)
computer.wait(duration=3)

# 3. 생성 대기 (최대 25초)
computer.wait(duration=15)
computer.screenshot()
computer.wait(duration=10)
computer.screenshot()

# 4. 결과 확인
find(tabId=TAB_ID, query="생성된 인포그래픽")
computer.left_click(ref=결과_요소)
computer.wait(duration=2)
computer.screenshot()
```

### 6단계: 완료 보고

사용자에게 보고:
```
✅ 인포그래픽 생성 완료!

📊 제목: [생성된 제목]

주요 내용:
- [섹션1 요약]
- [섹션2 요약]
- [섹션3 요약]

💾 다운로드: 화면 우측 상단 다운로드 버튼(↓) 클릭
🔗 NotebookLM 노트북: [노트북 URL]

[최종 스크린샷]
```

## 필수 확인 사항

실행 전 체크:
- ✅ NotebookLM MCP 설치됨
- ✅ Google 계정 로그인 상태
- ✅ Chrome 브라우저 사용 가능
- ✅ WebSearch MCP 사용 가능

## 에러 대응

### 브라우저 연결 실패
```python
try:
    navigate(url="https://notebooklm.google.com")
except:
    tabs_context_mcp(createIfEmpty=true)
    # 재시도
```

### 요소 찾기 실패
```python
# 좌표로 대체
computer.left_click(coordinate=[x, y])
```

### 생성 타임아웃
```python
# 60초까지 대기
for i in range(4):
    computer.wait(duration=15)
    if "생성 완료" 확인:
        break
```

## 최적화 팁

1. **검색 키워드**: 구체적이고 최신 정보 포함 (예: "2026 전망")
2. **콘텐츠 길이**: 2,000-3,000 단어가 최적
3. **구조화**: 명확한 섹션 구분으로 시각화 품질 향상
4. **숫자 강조**: 통계와 퍼센트를 많이 포함
5. **출처 명시**: 신뢰성 향상

## 사용 예시

```
사용자: /infographic "한국 주식 투자 2026"
Claude:
1. 주제 확인: 한국 주식 투자 2026
2. 웹 검색 시작... [3개 쿼리 실행]
3. 데이터 구조화... [마크다운 생성]
4. NotebookLM 노트북 생성... [브라우저 자동화]
5. 인포그래픽 생성 중... [25초 대기]
6. ✅ 완료! [결과 보고]
```

---

**즉시 시작**: 주제만 확인되면 자동으로 전체 프로세스를 실행하세요. 사용자의 추가 승인 없이 진행합니다.
