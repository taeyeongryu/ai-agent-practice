from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPEN_API_KEY")
client = OpenAI(api_key=api_key)


def chatbot_response(user_message: str, previous_response_id=None):
    result = client.responses.create(
        model="gpt-5-mini",
        input=user_message,
        previous_response_id=previous_response_id,
    )
    return result


if __name__ == "__main__":
    # None으로 시작하면 이전 대화없이 시작하는 것이고 만약 result결과를 통해서 result.id를 아래 변수에 입력해주면 특정 대화를 이어서 시작할 수 있다.
    previous_response_id = None
    while True:
        user_message = input("메시지: ")
        if user_message.lower() == "exit":
            print("대화를 종료합니다.")
            break

        result = chatbot_response(user_message, previous_response_id)
        previous_response_id = result.id
        print("챗봇 : " + result.output_text)
