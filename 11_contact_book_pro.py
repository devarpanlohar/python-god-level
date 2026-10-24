import json
import os


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append({"name": name, "phone": phone, "email": email})

    save_contacts()


def view_contact():
    print("\n--- SAVED CONTACTS ---")
    if len(contacts) == 0:
        print("No contacts yet")
    for index, con in enumerate(contacts):
        print(f"Contact - {index + 1}")
        for key, value in con.items():
            print(f"  {key}: {value}")


def search_contact():
    if len(contacts) == 0:
        print("No contacts yet")
    search_term = input("Enter the name: ")
    for index, con in enumerate(contacts):
        if search_term.lower() in con["name"].lower():
            print(f"Contact found! Contact id is {index + 1}")
            for key, value in con.items():
                print(f"  {key}: {value}")
            break


def delete_contact():
    if len(contacts) == 0:
        print("No contacts yet")
    else:
        delete_term = input("Enter the name: ")
        for index, con in enumerate(contacts):
            if delete_term.lower() in con["name"].lower():
                print("Record found.")
                contacts.pop(index)
                break
        print("Entry deleted. No undone.")
    save_contacts()


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            return json.load(f)
    return []


def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=2)


contacts = load_contacts()

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact by name")
    print("4. Delete contact by name")
    print("5. Exit")

    choose = input("Choose an option: ")

    if choose == "1":
        add_contact()
        print("1 contact recorded.")
    elif choose == "2":
        view_contact()
    elif choose == "3":
        search_contact()
    elif choose == "4":
        delete_contact()
    elif choose == "5":
        print("Program exited...")
        break
    else:
        print("Invalid option")
