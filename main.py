import os
import sys

"""Write the two-sentence story to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-400 chars, exactly two sentences, deterministic.

STORY = ("Grandmother's recipe card for blackberry jam lists my full birth name "
         "under ingredients with a measurement of one cup. "
         "The jar in her pantry bears my name and a date three years before I was born.")

def validate(content: str) -> None:
    if not (1 <= len(content) <= 400):
        raise ValueError("length out of range")
    if not content.strip():
        raise ValueError("empty after strip")
    if content.count('\n') != 1:
        raise ValueError("newline count != 1")
    if not content.endswith('\n'):
        raise ValueError("does not end with newline")
    if sum(content.count(c) for c in '.!?') != 2:
        raise ValueError("sentence terminator count != 2")

def main() -> None:
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'entry.txt')
    content = STORY + '\n'
    validate(content)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(out_path, len(content))

if __name__ == '__main__':
    main()
