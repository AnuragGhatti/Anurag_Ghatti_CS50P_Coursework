import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", ip)
    if not match:
        return False
    return all(0 <= int(match.group(i)) <= 255 for i in range(1, 5))


if __name__ == "__main__":
    main()
