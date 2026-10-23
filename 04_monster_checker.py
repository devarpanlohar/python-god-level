age = int(input("Enter your age: "))
dream = input("What is your dream?: ")

print("\n")
if age < 13:
    print("You are too young, but you can start early!")
elif age >= 13 and age <= 17:
    print("Teen coder-perfect time to start")
else:
    print("Adult monster mode ON")

if "python" in dream.lower():
    print("Python path confirmed -> Welcome to the club")
else:
    print("Cool dream! Python can help you build it")
