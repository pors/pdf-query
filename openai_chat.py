#!/usr/bin/env python3
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def chat_with_openai(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter your message: ")
    response = chat_with_openai(user_input)
    print(f"\nAssistant: {response}")