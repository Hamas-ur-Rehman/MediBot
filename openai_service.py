from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


def AskAI(messages:list):
    client = OpenAI()
    response = client.chat.completions.create(
    temperature=0,
    model="gpt-3.5-turbo",
    messages=messages
    )
    return response.choices[0].message.content