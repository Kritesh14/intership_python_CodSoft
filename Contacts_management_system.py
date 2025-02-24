import json

# File to store contacts persistently
CONTACTS_FILE = "contacts.json"

# Load contacts from file if exists
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}")

# Search contact by name or phone
def search_contact():
    query = input("Enter name or phone number to search: ")
    
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["Phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
    
    if not found:
        print("Contact not found.")

# Update contact details
def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        print("Leave field empty to keep current value.")
        phone = input(f"New phone ({contacts[name]['Phone']}): ") or contacts[name]["Phone"]
        email = input(f"New email ({contacts[name]['Email']}): ") or contacts[name]["Email"]
        address = input(f"New address ({contacts[name]['Address']}): ") or contacts[name]["Address"]

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")


# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
def main():
    global contacts
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")


        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
