def create_contact():

  name = input("Enter contact name: ")
  phone_number = input("Enter phone number: ")
  email = input("Enter email (optional): ")
  address = input("Enter address (optional): ")
  return {"name": name, "phone_number": phone_number, "email": email, "address": address}

def view_contacts(contacts):
    if contacts:
        print("\nContacts:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. {contact['name']} - {contact['phone_number']}")
    else:
        print("There are no contacts saved yet.")

def search_contact(contacts, search_term):
    matching_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone_number"]:
            matching_contacts.append(contact)
            return matching_contacts

def update_contact(contacts):
    if contacts:
        view_contacts(contacts)
        contact_index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            updated_contact = create_contact()
            contacts[contact_index] = updated_contact
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    else:
        print("There are no contacts saved yet.")
        return contacts

def delete_contact(contacts):

  if contacts:
    view_contacts(contacts)
    contact_index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= contact_index < len(contacts):
      del contacts[contact_index]
      print("Contact deleted successfully!")
    else:
      print("Invalid contact number.")
  else:
    print("There are no contacts saved yet.")
  return contacts

def main():
  contacts = []

  while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      new_contact = create_contact()
      contacts.append(new_contact)
      print("Contact added successfully!")
    elif choice == '2':
      view_contacts(contacts)
    elif choice == '3':
      search_term = input("Enter name or phone number to search: ")
      matching_contacts = search_contact(contacts, search_term)
      if matching_contacts:
        print("\nMatching Contacts:")
        for contact in matching_contacts:
          print(f"- {contact['name']} - {contact['phone_number']}")
      else:
        print("No contacts found.")
    elif choice == '4':
      contacts = update_contact(contacts)
    elif choice == '5':
      contacts = delete_contact(contacts)
    elif choice == '6':
      print("Exiting the program.")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
