# 💻 TokenSaver  

[![PyPI version](https://badge.fury.io/py/tokensaver.svg)](https://pypi.org/project/tokensaver/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Hugging Face Space](https://img.shields.io/badge/🤗%20HuggingFace-TokenSaver-orange)](https://huggingface.co/spaces/grittai/tokensaver)  

---

## 📖 Overview  

**TokenSaver** is a lightweight Python library + CLI tool to **minimize LLM token usage** before sending prompts to GPT, Claude, Mistral, etc.  

Every unnecessary **newline, space, or repeated entity** increases your LLM bill. TokenSaver preprocesses text and JSON to make them as compact as possible — **cutting costs without losing meaning**.  

---

## ✨ Features  

- 🧹 **Text Cleaning** → collapse whitespace, normalize newlines  
- 📦 **JSON Minify** → compact JSON into a single line  
- 🏷 **Entity Compression** → replace long repeated names/entities with short placeholders  

---

## 📦 Installation  

```bash
pip install tokensaver
```

---

## 🚀 Usage  

### 1. Python API  

```python
from tokensaver import clean_text, minify_json, compress_entities

# --- Text Cleaning ---
messy = "Hello     World   \n\nThis   is   a test.   "
print(clean_text(messy))
# -> "Hello World\nThis is a test."

# --- JSON Minify ---
pretty_json = """{
  "name": "John Doe",
  "age": 30,
  "skills": [
    "Python",
    "AI"
  ]
}"""

print(minify_json(pretty_json))
# -> {
#   'result': {'name': 'John Doe', 'age': 30, 'skills': ['Python', 'AI']},
#   'minified': '{"name":"John Doe","age":30,"skills":["Python","AI"]}'
# }

# --- Entity Compression ---
entity_text = """The International Business Machines Corporation 
makes enterprise software. International Business Machines Corporation 
is also known as IBM."""

print(compress_entities(entity_text))
# -> {
#   'compressed': 'E1 makes enterprise software. E1 is also known as IBM.',
#   'mapping': {'International Business Machines Corporation': 'E1'}
# }
```

---

### 2. CLI Usage  

When installed, TokenSaver also provides a **command-line tool**:

```bash
# Clean messy text
tokensaver clean "Hello     World"
# -> "Hello World"

# Minify JSON
tokensaver json '{"name":"John","age":30}'
# -> {"result": {"name": "John", "age": 30}, "minified": "{\"name\":\"John\",\"age\":30}"}

# Compress repeated entities
tokensaver entities "International Business Machines Corporation makes software. International Business Machines Corporation sells software."
# -> {"compressed": "E1 makes software. E1 sells software.", "mapping": {"International Business Machines Corporation": "E1"}}
```

---

## 🧑‍💻 Why TokenSaver?  

Every token costs 💰. Formatting intended for **humans** (pretty-printed JSON, repeated names, redundant whitespace) doesn’t help AI models — but **does** increase token count.  

**TokenSaver** helps you:  
- Minimize cost for API calls  
- Preprocess logs, transcripts, or JSON before sending to LLMs  
- Keep your pipelines fast & efficient  

---

## 🔗 Links  

- 🤗 [Hugging Face Demo](https://huggingface.co/spaces/grittai/tokensaver)  
- 📦 [PyPI Package](https://pypi.org/project/tokensaver/)  
- 💻 [Source Code](https://github.com/grittcloud/tokensaver)  

---

## 📝 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  
