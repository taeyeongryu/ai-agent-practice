import asyncio
import os
import logging
import random

from openai import AsyncOpenAI
from dotenv import load_dotenv
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")
client = AsyncOpenAI(api_key=api_key)


async def simulate_random_failure():
    if random.random() < 0.5:
        logger.warning("인위적으로 api 호출 실패 발생 (테스트 용)")
        raise ConnectionError("인위적으로 발생시킨 연결 오류 (테스트용)")
    # 지연시간 추가
    await asyncio.sleep(random.uniform(0.1, 0.5))


@retry(
    stop=stop_after_attempt(3),
    wait=wait_random_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(Exception),
    before_sleep=lambda retry_state: logger.warning(
        f"api 호출 실패: {retry_state.outcome.exception()}, {retry_state.attempt_number}번째 재시도 중..."
    ),
)
async def call_async_openai_5mini(prompt: str, model: str = "gpt-5-mini") -> str:

    logger.info(f"5mini API 호출 시작: {model}")
    await simulate_random_failure()

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
    )
    logger.info(f"5mini API 호출 완료: {model}")
    return response.choices[0].message.content


async def call_async_openai_4o(prompt: str, model: str = "gpt-4o") -> str:
    logger.info(f"4o API 호출 시작: {model}")

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
    )
    logger.info(f"4o API 호출 완료: {model}")
    return response.choices[0].message.content


async def main():
    print("동시에 api 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."

    openai_task_5mini = call_async_openai_5mini(prompt)
    openai_task_4o = call_async_openai_4o(prompt)

    try:
        response_5mini, response_4o = await asyncio.gather(
            openai_task_5mini, openai_task_4o, return_exceptions=False
        )
        print(f"5mini: {response_5mini}")
        print(f"4o: {response_4o}")
    except Exception as e:
        logger.error(f"api 호출 중 처리되지 않은 오류 발생: {e}")


if __name__ == "__main__":
    asyncio.run(main())
