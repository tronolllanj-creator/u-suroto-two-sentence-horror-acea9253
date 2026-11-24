"""Entrypoint module for the grader."""
# Entry validated: output is 1-400 chars, exactly two sentences, deterministic.

import os
import sys

STORY = "The smoke detector on the ceiling only gives its sharp, two-tone chirp when I am fast asleep and dreaming of open windows. My wife insists she stays awake all night just to watch the little red LED blink against the dark."


def main():
    base_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(base_dir, exist_ok=True)
    file_path = os.path.join(base_dir, "entry.txt")

    content = STORY + chr(10)
    stripped_story = STORY.strip()

    if not stripped_story:
        raise ValueError("Story is only whitespace")

    if len(content) > 400 or len(content) < 1:
        raise ValueError("Invalid length")

    sentence_count = 0
    length = len(stripped_story)
    for i in range(length):
        char = stripped_story[i]
        if char in ".!?":
            if i == length - 1 or stripped_story[i + 1] == " ":
                sentence_count += 1

    if sentence_count != 2:
        raise ValueError("Invalid sentence count")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(file_path)
    print(len(content))
    print(sentence_count)


if __name__ == "__main__":
    main()
