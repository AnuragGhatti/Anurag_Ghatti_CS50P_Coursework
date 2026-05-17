import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )
    if not match:
        raise ValueError("Invalid format")

    start_h, start_m, start_period, end_h, end_m, end_period = match.groups()

    start_h = int(start_h)
    start_m = int(start_m) if start_m else 0
    end_h = int(end_h)
    end_m = int(end_m) if end_m else 0

    if not (1 <= start_h <= 12 and 0 <= start_m <= 59):
        raise ValueError("Invalid start time")
    if not (1 <= end_h <= 12 and 0 <= end_m <= 59):
        raise ValueError("Invalid end time")

    start_h = to_24(start_h, start_period)
    end_h = to_24(end_h, end_period)

    return f"{start_h:02}:{start_m:02} to {end_h:02}:{end_m:02}"


def to_24(hour, period):
    if period == "AM":
        return 0 if hour == 12 else hour
    else:  # PM
        return 12 if hour == 12 else hour + 12


if __name__ == "__main__":
    main()
