import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

number = random.randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
