# 🤖 AI Agent Practice

2026년, AI 관련 역량을 키우기 위해 시작한 학습 프로젝트입니다.  
책 **[요즘 AI 에이전트](https://product.kyobobook.co.kr/detail/S000217241525)**의 예제를 직접 실습하고 기록하는 공간입니다.

---

## 🎯 학습 목표
- AI 에이전트의 핵심 원리 이해
- LLM(Large Language Model) API 활용 능력 배양
- 실전 에이전트 서비스 구현 및 배포 실습

## 📂 프로젝트 구조
- **chapter1/**: OpenAI API 기초 (Hello World 실습)
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
루트 폴더에 `.env` 파일을 생성하고 API 키를 입력하세요.
```env
OPEN_API_KEY=your_actual_api_key_here
```

---
*본 레포지토리는 개인적인 학습 목적으로 운영됩니다.*