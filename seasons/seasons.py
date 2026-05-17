# seasons.py

from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birthdate = input("Date of Birth: ").strip()

    try:
        minutes = get_minutes(birthdate)
        print(convert_to_words(minutes))
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(birthdate):
    try:
        year, month, day = map(int, birthdate.split("-"))
        dob = date(year, month, day)
    except:
        raise ValueError

    today = date.today()
    delta = today - dob

    return delta.days * 24 * 60


def convert_to_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
