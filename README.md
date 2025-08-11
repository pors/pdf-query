# PDF Analysis Scripts - OpenAI API

## Overview
This repository contains scripts for analyzing PDF documents using OpenAI's new **Responses API**.

## Available Scripts

### 1. `pdf_simple.py` ✅
- Simple example with hardcoded filename and question
- Uses the new **Responses API** - no deprecation warnings
- Good for quick testing and understanding the API

### 2. `pdf_query.py` ✅
- Full-featured command-line tool
- Uses the new **Responses API** - no deprecation warnings  
- Flexible arguments and error handling
- Production-ready

Usage:
```bash
# With direct question
python pdf_query.py document.pdf -q "What are the main topics?"

# Interactive mode (will prompt for question)
python pdf_query.py document.pdf
```

## Requirements

1. **OpenAI Python Library v1.99.6+**
   ```bash
   pip install --upgrade openai
   ```

2. **Environment Variable**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Supported Models
- gpt-4o
- gpt-4o-mini
- o1 (and other vision-capable models)

## Limitations
- Maximum 100 pages per PDF
- Maximum 32MB total content per request
- Only vision-capable models support PDF input

## Troubleshooting
If you get API errors:
- Check that your API key is set correctly
- Verify the PDF file exists and is under 32MB
- Ensure you're using a vision-capable model