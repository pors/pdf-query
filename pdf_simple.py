#!/usr/bin/env python3
"""
Fixed version using the new Responses API - no deprecation warnings
"""
import os
import base64
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
filename = "1754732146545.pdf"
prompt = "What are the main topics of this document?"

# Read and encode PDF as base64
with open(filename, "rb") as pdf_file:
    pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

# Use the new Responses API with direct PDF input (no deprecation warnings)
response = client.responses.create(
    model="gpt-4o-mini",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": prompt},
            {
                "type": "input_file",
                "filename": filename,
                "file_data": f"data:application/pdf;base64,{pdf_base64}"
            }
        ]
    }]
)

# Extract and print the response text
if response.output and len(response.output) > 0:
    print(response.output[0].content[0].text)
else:
    print("No response generated")