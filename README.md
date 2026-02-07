# 🤖 AI Agent Practice

2026년, AI 관련 역량을 키우기 위해 시작한 학습 프로젝트입니다.  
책 **[요즘 AI 에이전트](https://product.kyobobook.co.kr/detail/S000217241525)**의 예제를 직접 실습하고 기록하는 공간입니다.

---

## 🎯 학습 목표
- AI 에이전트의 핵심 원리 이해
- LLM(Large Language Model) API 활용 능력 배양
- 실전 에이전트 서비스 구현 및 배포 실습
- LangGraph를 활용한 복잡한 워크플로우 제어 습득

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
    - `langchain_runnable_branch.py`: 입력 조건에 따라 다른 체인을 실행하는 분기 처리 실습
    - `langchain_structured_output.py`: Pydantic을 활용한 구조화된 데이터(JSON) 출력 실습
    - **embedding/**: 텍스트 임베딩 및 벡터 데이터베이스 실습
      - `my_first_embedding.py`: OpenAI를 이용한 텍스트 임베딩 생성 및 코사인 유사도 계산 기초
      - `embedding_with_vectorstore.py`: FAISS 벡터스토어를 활용한 텍스트 검색 및 유사도 계산
      - `vectorstore_with_document.py`: Document 객체를 활용한 벡터스토어 구축 및 검색
      - `retriever_from_vectorstore.py`: 벡터스토어를 리트리버(Retriever)로 변환하여 RAG 체인 구성
    - **retriever_rag/**: 리트리버 기반의 RAG(Retrieval-Augmented Generation) 실습
      - `rag_by_duckduckgo.py`: DuckDuckGo 검색 도구를 활용한 실시간 웹 정보 기반 RAG 구현
  </details>
- **chapter4/**: OpenAI 에이전트 실습
  <details>
  <summary>세부 파일 목록</summary>

    - **openai-agent-sdk/**: OpenAI의 실험적 Swarm 프레임워크 스타일 구현
      - `hello_agent_sync.py`: 기본적인 동기식 에이전트 실행
      - `news_search_agent.py`: 외부 도구(DuckDuckGo)를 사용하는 뉴스 검색 에이전트
      - `input_output_guardrail_test.py`: 입출력 가드레일 테스트
      - `simple_multi_agent_by_handoff.py`: Handoff 패턴을 이용한 멀티 에이전트
  </details>
- **chapter5/**: 구글 AI 에이전트 실습
  <details>
  <summary>세부 파일 목록</summary>

    - `hello-agent/`: Google의 Agent SDK 기반 기초 실습
    - `multi-agent-for-bestselller-book/`: 베스트셀러 도구 검색 멀티 에이전트
  </details>
- **chapter6/**: 랭그래프(LangGraph) 심화
  <details>
  <summary>세부 파일 목록</summary>

    - `02_conditional_routing.py`: 조건부 라우팅 구현
    - `03_persistent_memory.py`: 영구 메모리(Checkpointer) 활용
    - `04_loop_workflow.py`: 순환(Loop) 워크플로우 제어
    - `06_tool_calling.py`: 에이전트의 도구 호출 메커니즘
    - `07_human_in_loop.py`: 인간 개입(Interrupt/Breakpoints) 시스템
  </details>
- **chapter9/**: 실전 프로젝트 - Google News AI 멀티에이전트
  <details>
  <summary>시스템 특징</summary>

    - **RSSCollector**: 구글 뉴스 RSS 수집 및 실제 본문 스크래핑
    - **Summarizer**: 수집된 뉴스 내용 요약 (OpenAI 활용)
    - **Organizer**: 카테고리 분류 및 중복 기사 정리
    - **Reporter**: 최종 마크다운 형식의 일일 뉴스 리포트 생성
  </details>
- **chapter10/**: MCP(Model Context Protocol) 시스템
  <details>
  <summary>시스템 구성</summary>

    - `mcp_server.py`: FastMCP를 이용한 도구 제공 서버 (날씨, 뉴스, 야구 순위 등)
    - `chat_agent.py`: MCP 서버에 연결된 스트리밍 채팅 에이전트 및 웹 UI (FastAPI)
  </details>

## 🚀 시작하기

### 1. 환경 설정
이 프로젝트는 **Python 3.13.2** 버전을 사용합니다.

**가상환경 생성 및 활성화:**

- **Windows:**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\activate
  ```

**의존성 설치:**
```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정
`.env` 파일에 발급받은 API 키를 입력하세요.

```env
OPENAI_API_KEY=your_actual_api_key_here
```

---
*본 레포지토리는 개인적인 학습 목적으로 운영되며 모든 클론 코딩 실습이 완료되었습니다.*
