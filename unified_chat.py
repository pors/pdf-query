#!/usr/bin/env python3
import os
import argparse
from openai import OpenAI

def create_xai_client():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise ValueError("XAI_API_KEY environment variable is not set")
    return OpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1",
    )

def create_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    return OpenAI(api_key=api_key)

def chat(provider, message):
    if provider == "xai":
        client = create_xai_client()
        model = "grok-3-mini"
        system_message = "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        response_label = "Grok"
    else:  # openai
        client = create_openai_client()
        model = "gpt-4o-mini"
        system_message = "You are a helpful assistant."
        response_label = "Assistant"
    
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": message},
        ],
    )
    
    return completion.choices[0].message.content, response_label

def main():
    parser = argparse.ArgumentParser(description="Chat with xAI or OpenAI")
    parser.add_argument(
        "provider",
        choices=["xai", "openai"],
        help="Choose the AI provider (xai or openai)"
    )
    parser.add_argument(
        "-m", "--message",
        type=str,
        help="Message to send (if not provided, will prompt for input)"
    )
    
    args = parser.parse_args()
    
    if args.message:
        user_input = args.message
    else:
        user_input = input("Enter your message: ")
    
    try:
        response, label = chat(args.provider, user_input)
        print(f"\n{label}: {response}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()