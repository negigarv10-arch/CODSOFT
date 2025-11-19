contacts = []

def add_contact():
    """Allows user to add a new contact with details."""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(new_contact)
    print(f"\n✅ Contact '{name}' added successfully.")

def view_contacts():
    """Displays a list of all saved contacts (Name and Phone)."""
    if not contacts:
        print("\nYour Contact Book is empty.")
        return
    
    print("\n--- CONTACT LIST ---")
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("--------------------")

def search_contact():
    """Searches for a contact by name or phone number."""
    term = input("Enter name or phone number to search: ").lower()
    found_contacts = []
    
    for contact in contacts:
        # Check if the search term is in the name or phone number
        if term in contact['name'].lower() or term in contact['phone']:
            found_contacts.append(contact)

    if found_contacts:
        print("\n--- SEARCH RESULTS ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("\nNo contact found with that name or number.")

def delete_contact():
    """Deletes a contact by their index."""
    view_contacts()
    if not contacts:
        return

    try:
        index_to_delete = int(input("Enter the NUMBER of the contact to DELETE: ")) - 1
        
        if 0 <= index_to_delete < len(contacts):
            deleted_contact = contacts.pop(index_to_delete)
            print(f"\n🗑️ Contact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("\n❌ Invalid contact number.")
    except ValueError:
        print("\n❌ Please enter a valid number.")

def main():
    """Main function to run the Contact Book application."""
    print("Welcome to your Python Contact Book!")
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()