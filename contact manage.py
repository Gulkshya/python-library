import json
import os

FILENAME = 'contacts.json'

def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"{name} - Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

contacts = load_contacts()

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid option.")
