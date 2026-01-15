import asyncio
import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")
client = AsyncOpenAI(api_key=api_key)


async def call_async_openai_5mini(prompt: str, model: str = "gpt-5-mini") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
    )
    return response.choices[0].message.content


async def call_async_openai_4o(prompt: str, model: str = "gpt-4o") -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
    )
    return response.choices[0].message.content


async def main():
    print("동시에 api 호출하기")
    prompt = "비동기 프로그래밍에 대해 두세 문장으로 설명해주세요."

    openai_task_5mini = call_async_openai_5mini(prompt)
    openai_task_4o = call_async_openai_4o(prompt)

    response_5mini, response_4o = await asyncio.gather(
        openai_task_5mini, openai_task_4o
    )
    print(f"5mini: {response_5mini}")
    print(f"4o: {response_4o}")


if __name__ == "__main__":
    asyncio.run(main())
