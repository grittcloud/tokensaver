import re
import json
from collections import defaultdict

MAX_INPUT_SIZE = 50000  # 50KB limit

def clean_text(text: str) -> str:
    """Collapse whitespace/newlines and strip extra spaces."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()

def minify_json(json_str: str):
    """Return parsed + minified JSON, or error if invalid."""
    try:
        obj = json.loads(json_str)
        return {"result": obj, "minified": json.dumps(obj, separators=(",", ":"))}
    except Exception as e:
        return {"error": f"Invalid JSON: {str(e)}", "cleaned": clean_text(json_str)}

def compress_entities(text: str):
    """Replace long repeated entities with placeholders."""
    words = re.findall(r'\b[A-Z][a-zA-Z]{5,}(?: [A-Z][a-zA-Z]{2,}){1,}\b', text)
    counts = defaultdict(int)
    for w in words:
        counts[w] += 1
    replacements = {entity: f"E{i+1}" for i, (entity, c) in enumerate(counts.items()) if c > 1}
    compressed = text
    for entity, placeholder in replacements.items():
        compressed = compressed.replace(entity, placeholder)
    return {"compressed": compressed, "mapping": replacements}
