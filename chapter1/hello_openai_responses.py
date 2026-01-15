from openai import OpenAI
from dotenv import load_dotenv

import os
import sys

# Set stdout to UTF-8 for Windows console compatibility
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(api_key=api_key)


def get_responses(prompt, model):
    response = client.responses.create(
        model=model,
        tools=[{"type": "web_search"}],
        input=prompt,
    )
    return response.output_text


if __name__ == "__main__":
    prompt = """
    https://platform.openai.com/docs/api-reference/responses/create 를 읽어서 리스폰스 api에 대해 요약 정리해주세요."""

    output = get_responses(prompt, model="gpt-5-mini")
    print(output)
