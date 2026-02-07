import os

class Config:
    """프로젝트 설정 관리 클래스"""

    #openai 설정
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME: str = "gpt-4o-mini"
    MAX_TOKENS: int = 150

    ROOT_DIR :str= os.path.dirname(os.path.abspath(__file__))

    RSS_URL: str = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    MAX_NEWS_COUNT: int = 60

    BATCH_SIZE: int = 10

    NEWS_CATEGORIES: list[str] = ["경제", "정치", "사회", "생활/문화", "IT/과학", "외교"]

    NEWS_PER_CATEGORY: int = 30
    OUTPUT_DIR: str = f"{ROOT_DIR}/outputs"

    @classmethod
    def validate(cls)->bool:
        """설정 값 유효성 검사"""
        if not cls.OPENAI_API_KEY:
            print("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
            print("환경 변수를 설정하고 다시 실행하세요.")
            return False
        return True