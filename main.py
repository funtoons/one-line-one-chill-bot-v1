"""One Line, One Chill - entry v1.

Writes a single sentence of horror to /output/entry.txt.
Deterministic, stdlib-only, offline: the line is a fixed constant.
"""

LINE = (
    "The dentist found a second row of teeth growing behind mine \u2014 "
    "and they were already chewing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
