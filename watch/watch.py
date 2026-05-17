import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*\ssrc="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if not match:
        return None
    return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
