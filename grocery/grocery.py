grocery = {}

while True:
    try:
        item = input("").strip().upper()
        grocery[item] = grocery.get(item, 0) + 1
    except EOFError:
        print()
        break

for item in sorted(grocery):
    print(f"{grocery[item]} {item}")
