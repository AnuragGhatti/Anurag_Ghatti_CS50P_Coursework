def main():
    x, y, z = input("Expression: ").split()

    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
