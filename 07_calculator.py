def user_input():
    a = int(input("Enter first number: "))
    b = int(input("Enter second: "))
    return a, b


def add():
    a, b = user_input()
    return f"Result: {a} + {b} = {a + b}"


def subtract():
    a, b = user_input()
    return f"Result: {a} - {b} = {a - b}"


def multiply():
    a, b = user_input()
    return f"Result: {a} x {b} = {a * b}"


def divide():
    a, b = user_input()
    if b == 0:
        return "Cannot divide by zero"
    return f"Result: {a} / {b} = {a / b}"


def show_menu():
    print("\n--- Function-Powered CLI Calculator---")
    print("1. Add")
    print("2. Subtaract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        print(add())
    elif choice == "2":
        print(subtract())
    elif choice == "3":
        print(multiply())
    elif choice == "4":
        print(divide())
    elif choice == "5":
        print("Program exited")
        break
    else:
        print("Invalid option")
