import random

secret = random.randint(1, 100)
attempt = 0

print("I'm thinking of a number 1-100...")
while True:
    num = int(input("Enter a guess: "))
    attempt += 1
    if num < secret:
        print("Too low! Go higher")
    elif num > secret:
        print("Too high! Go lower")
    else:
        print(f"BOOM! You guessed it in {attempt} attempts")
        break
