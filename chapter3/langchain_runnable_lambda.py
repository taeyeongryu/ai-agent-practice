from langchain_core.runnables import RunnableLambda


def add_exclamation(text: str) -> str:
    return f"{text}!"


exclamation_runnable = RunnableLambda(add_exclamation)

result = exclamation_runnable.invoke("안녕하세요")
print(result)

result = exclamation_runnable.batch(["안녕", "반가워", "잘가"])
print(result)
