from dotenv import load_dotenv
from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-5-mini")

parser = StrOutputParser()

def is_english(x: dict) -> bool:
    """입력 딕셔너리의 'word' 키에 해당하는 값이 영어 단어인지 확인합니다."""
    return all(ord(char) < 128 for char in x["word"])
english_prompt = ChatPromptTemplate.from_template(
    "Give me 3 synonyms for {word}. Only list the words"
)
korean_prompt = ChatPromptTemplate.from_template(
    "주어진 '{word}'의 동의어 3개를 한국어로 제시해 주세요. 단어만 나열하세요."
)

# 조건부 분기를 정의
# is_english 함수가 True를 반환하면 영어 프롬프트를 사용하고, 그렇지 않으면 한국어 프롬프트를 사용합니다.
language_aware_chain = RunnableBranch(
    (is_english, english_prompt|model|parser),
    korean_prompt|model|parser
)

english_word = {"word": "happy"}
english_result = language_aware_chain.invoke(english_word)
print(f"English synonyms for '{english_word['word']}': {english_result}")

korean_word = {"word": "행복"}
korean_result = language_aware_chain.invoke(korean_word)
print(f"Korean synonyms for '{korean_word['word']}': {korean_result}")

