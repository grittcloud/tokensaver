import argparse
from .core import clean_text, minify_json, compress_entities

def main():
    parser = argparse.ArgumentParser(description="TokenSaver - Minimize LLM token usage")
    parser.add_argument("mode", choices=["clean", "json", "entities"], help="Processing mode")
    parser.add_argument("input", help="Input string or file")
    parser.add_argument("--file", action="store_true", help="Read input from a file")
    args = parser.parse_args()

    text = open(args.input).read() if args.file else args.input

    if args.mode == "clean":
        print(clean_text(text))
    elif args.mode == "json":
        print(minify_json(text))
    elif args.mode == "entities":
        print(compress_entities(text))

if __name__ == "__main__":
    main()
