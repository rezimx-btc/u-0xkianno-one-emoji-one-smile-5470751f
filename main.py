#!/usr/bin/env python3
"""One Emoji, One Smile.

Prints exactly one emoji to stdout: the warmest, most instantly
readable smile. Stdlib only, deterministic, no arguments, no input,
no trailing output beyond the single newline print() adds.
"""

EMOJI = "\U0001F60A"  # 😊 smiling face with smiling eyes


def main() -> None:
    print(EMOJI)


if __name__ == "__main__":
    main()
