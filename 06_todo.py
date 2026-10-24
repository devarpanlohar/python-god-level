tasks = []

while True:
    print("\n--- TO-DO MANAGER ---")
    print("1. View tasks")
    print("2. Add tasks")
    print("3. Remove tasks")
    print("4. Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for task in tasks:
                print(f"- {task}")
    elif choice == " 2":
        new_task = input("What is your task?: ")
        tasks.append(new_task)
    elif choice == "3":
        for id, task in enumerate(tasks):
            print(f"{id + 1}. {task}")
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)
    elif choice == "4":
        print("Bye monster!")
        break
    else:
        print("Invalid choice")
