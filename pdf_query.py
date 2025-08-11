#!/usr/bin/env python3
"""
PDF analysis using OpenAI's new Responses API (no deprecation warnings)
This replaces the deprecated Assistants API approach.
"""
import os
import argparse
import base64
from openai import OpenAI

def query_pdf_with_responses_api(pdf_path, question):
    """Analyze PDF using the new Responses API."""
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Read and encode PDF as base64
    with open(pdf_path, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')
    
    # Use the Responses API with direct PDF input
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{
            "role": "user",
            "content": [
                {"type": "input_text", "text": question},
                {
                    "type": "input_file",
                    "filename": os.path.basename(pdf_path),
                    "file_data": f"data:application/pdf;base64,{pdf_base64}"
                }
            ]
        }]
    )
    
    # Extract text from response
    if response.output and len(response.output) > 0:
        return response.output[0].content[0].text
    return "No response generated"

def main():
    parser = argparse.ArgumentParser(
        description="Query a PDF using OpenAI's Responses API (no deprecation warnings)"
    )
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    parser.add_argument(
        "-q", "--question",
        type=str,
        help="Question about the PDF (if not provided, will prompt for input)"
    )
    
    args = parser.parse_args()
    
    # Check if PDF file exists
    if not os.path.exists(args.pdf_path):
        print(f"Error: PDF file '{args.pdf_path}' not found")
        return
    
    # Get question
    question = args.question or input("Enter your question about the PDF: ")
    
    try:
        print(f"\nAnalyzing PDF: {args.pdf_path}")
        print(f"Question: {question}\n")
        print("Processing...\n")
        
        response = query_pdf_with_responses_api(args.pdf_path, question)
        print(f"Answer:\n{response}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()