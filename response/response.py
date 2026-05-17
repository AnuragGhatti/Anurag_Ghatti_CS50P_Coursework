import validators


def main():
    email = input("Email: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


main()
