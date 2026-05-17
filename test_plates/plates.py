def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    seen_number = False

    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and not seen_number:
                return False
            seen_number = True
        elif char.isalpha():
            if seen_number:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
