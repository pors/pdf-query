#!/usr/bin/env python3
import os
from openai import OpenAI

XAI_API_KEY = os.getenv("XAI_API_KEY")
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY environment variable is not set")

client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def chat_with_xai(message):
    completion = client.chat.completions.create(
        model="grok-3-mini",
        messages=[
            {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter your message: ")
    response = chat_with_xai(user_input)
    print(f"\nGrok: {response}")