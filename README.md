# 🤖 AI Agent Practice

2026년, AI 관련 역량을 키우기 위해 시작한 학습 프로젝트입니다.  
책 **[요즘 AI 에이전트](https://product.kyobobook.co.kr/detail/S000217241525)**의 예제를 직접 실습하고 기록하는 공간입니다.

---

## 🎯 학습 목표
- AI 에이전트의 핵심 원리 이해
- LLM(Large Language Model) API 활용 능력 배양
- 실전 에이전트 서비스 구현 및 배포 실습

## 📂 프로젝트 구조
- **chapter1/**: OpenAI API 기초 및 실습
  <details>
  <summary>세부 파일 목록</summary>

    - `hello_openai.py`: 기본적인 텍스트 생성 실습
    - `hello_openai_responses.py`: OpenAI Responses API 활용 실습
    - `hello_openai_streaming.py`: 스트리밍(Streaming) 방식의 응답 구현
    - `async_llm_api.py`: `asyncio`를 이용한 비동기 API 호출 병렬 처리
  </details>
- **chapter2/**: 페르소나 챗봇 만들기 (어린 왕자)
  <details>
  <summary>세부 파일 목록</summary>

    - `chatbot3_little_prince.py`: CLI 기반의 어린 왕자 페르소나 챗봇
    - `chatbot4_little_prince_web_ui.py`: FastAPI를 활용한 웹 UI 버전 챗봇
  </details>
- **chapter3/**: 랭체인(LangChain) 입문
  <details>
  <summary>세부 파일 목록</summary>

    - `hello_langchain.py`: LangChain을 이용한 기본 Chat Model 호출 실습
    - `langchain_messages.py`: System, Human, AI Message 객체 활용 실습
    - `langchain_prompt_template_and_output_parser.py`: PromptTemplate과 OutputParser를 활용한 체인 구성
    - `langchain_runnable_lambda.py`: 사용자 정의 함수(Python Function)를 체인에 통합하는 방법
    - `langchain_runnable_parallel.py`: 여러 작업을 병렬로 수행하는 RunnableParallel 실습
    - `langchain_runnable_passthrough.py`: 체인 중간에 데이터를 그대로 전달하거나 추가하는 기법
    - `langchain_structured_output.py`: Pydantic을 활용한 구조화된 데이터(JSON) 출력 실습
  </details>
- **.venv/**: 프로젝트 전용 가상환경 (Python 3.13.2)

## 🚀 시작하기

### 1. 환경 설정
이 프로젝트는 **Python 3.13.2** 버전을 사용합니다.

**가상환경 생성 및 활성화:**

- **Windows:**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\activate
  ```
- **Mac / Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

**의존성 설치:**
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
`.env.example` 파일을 복사하여 `.env` 파일을 생성하고, 발급받은 API 키를 입력하세요.

**Windows:**
```powershell
copy .env.example .env
```

**Mac / Linux:**
```bash
cp .env.example .env
```

```env
OPEN_API_KEY=your_actual_api_key_here
```

---
*본 레포지토리는 개인적인 학습 목적으로 운영됩니다.*