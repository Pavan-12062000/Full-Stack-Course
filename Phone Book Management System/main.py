from datetime import datetime
from contact import Contact
from phonebook import PhoneBook
from validation import validate_email, validate_phone_number

def main():
    """Main function to manage the phonebook via command-line interface."""
    phonebook = PhoneBook()

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Import Contacts from CSV")
        print("8. Merge Two Contacts")
        print("9. Filter Contacts by Date")
        print("10. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':  # Add Contact
            print("\n** Type 'cancel' at any time to stop adding a contact and return to the main menu **")

            # Prompt and validate first name
            while True:
                first_name = input("First Name (Required): ").strip()
                if first_name.lower() == "cancel":
                    print("Add contact operation canceled. Returning to the main menu.")
                    break
                if first_name:
                    break
                print("Please enter First Name.")

            if first_name.lower() == "cancel":
                continue  # Skip to the main menu

            # Prompt and validate last name
            while True:
                last_name = input("Last Name (Required): ").strip()
                if last_name.lower() == "cancel":
                    print("Add contact operation canceled. Returning to the main menu.")
                    break
                if last_name:
                    break
                print("Please enter Last Name.")

            if last_name.lower() == "cancel":
                continue

            # Prompt and validate phone number
            phone_numbers = []
            while True:
                phone_number = input("Phone Number (Required) (###) ###-####: ").strip()
                if phone_number.lower() == "cancel":
                    print("Add contact operation canceled. Returning to the main menu.")
                    phone_numbers = []  # Reset phone numbers to avoid saving partial data
                    break
                if phone_number:
                    if validate_phone_number(phone_number):
                        phone_numbers.append(phone_number)
                    else:
                        print("Invalid phone number format. Please try again.")
                        continue
                else:
                    print("Please enter a phone number.")
                    continue

                while True:
                    add_more = input("Would you like to add another phone number? (y/n): ").strip().lower()
                    if add_more == "cancel":
                        print("Add contact operation canceled. Returning to the main menu.")
                        phone_numbers = []  # Reset phone numbers to avoid saving partial data
                        break  # Break out of the phone number addition loop
                    elif add_more == 'y':
                        break  # Continue the loop to add another phone number
                    elif add_more == 'n':
                        break  # Exit the phone number addition loop
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

                if add_more == "cancel":
                    break  # Exit the phone number addition loop if canceled
                if add_more == 'n':
                    break  # Exit the phone number addition loop if done adding phone numbers

            if not phone_numbers:
                print("You must enter at least one phone number.")
                continue  # Go back to the main menu if no phone numbers were provided

            # Prompt for optional email
            email = input("Email (Optional): ").strip()
            if email.lower() == "cancel":
                print("Add contact operation canceled. Returning to the main menu.")
                continue
            if email and not validate_email(email):
                print("Invalid email format. Skipping email.")
                email = None

            # Prompt for optional address
            address = input("Address (Optional): ").strip()
            if address.lower() == "cancel":
                print("Add contact operation canceled. Returning to the main menu.")
                continue

            contact = Contact(first_name, last_name, phone_numbers, email, address)
            phonebook.add_contact(contact)

        elif choice == '2':  # View Contacts
            phonebook.list_contacts()

        elif choice == '3':  # Search Contact
            print("\n** Type 'cancel' at any time to stop adding a contact and return to the main menu **")
            search_term = input("Enter search term: ").strip()
            if search_term.lower() == "cancel":
                print("Search operation canceled. Returning to the main menu.")
                continue
            else:
                results = phonebook.find_contact(search_term)
                if results:
                    for contact in results:
                        print(contact)
                else:
                    print("No matching contacts found.")

        elif choice == '4':  # Update Contact
            print("\n** Type 'cancel' at any time to stop updating a contact and return to the main menu **")
            search_term = input("Enter search term: ").strip()
            if search_term.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue
            first_name = input("New First Name (leave blank to keep current): ").strip()
            if first_name.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue
            last_name = input("New Last Name (leave blank to keep current): ").strip()
            if last_name.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue
            phone_number = input("New Phone Number (###) ###-#### (leave blank to keep current): ").strip()
            if phone_number.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue
            if phone_number and not validate_phone_number(phone_number):
                print("Invalid phone number format.")
                phone_number = None
            email = input("New Email (leave blank to keep current): ").strip()
            if email.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue
            if email and not validate_email(email):
                print("Invalid email format.")
                email = None
            address = input("New Address (leave blank to keep current): ").strip()
            if address.lower() == "cancel":
                print("Update operation canceled. Returning to the main menu.")
                continue

            phonebook.update_contact(search_term, first_name, last_name, phone_number, email, address)

        elif choice == '5':  # Delete Contact
            print("\n** Type 'cancel' at any time to stop deleting a contact and return to the main menu **")
            search_term = input("Enter search term: ").strip()
            if search_term.lower() == "cancel":
                print("Delete operation canceled. Returning to the main menu.")
                continue

            
            if phonebook.delete_contact(search_term):
                print("Contact deleted successfully.")
            else:
                print("Contact deletion operation was canceled or contact not found.")


        elif choice == '6':  # Export Contacts to CSV
            print("\n** Type 'cancel' at any time to stop exporting a contact and return to the main menu **")
            csv_file_path = input("Enter CSV file path: ").strip()
            if csv_file_path.lower() == "cancel":
                print("Export operation canceled. Returning to the main menu.")
                continue
            phonebook.export_contacts_to_csv(csv_file_path)

        elif choice == '7':  # Import Contacts from CSV
            print("\n** Type 'cancel' at any time to stop importing a contact and return to the main menu **")
            csv_file_path = input("Enter CSV file path: ").strip()
            if csv_file_path.lower() == "cancel":
                print("Import operation canceled. Returning to the main menu.")
                continue
            phonebook.import_contacts_from_csv(csv_file_path)

        elif choice == '8':  # Merge Two Contacts
            print("\n** Type 'cancel' at any time to stop merging a contact and return to the main menu **")
            full_name1 = input("Enter the first contact's full name: ").strip()
            if full_name1.lower() == "cancel":
                print("Merge operation canceled. Returning to the main menu.")
                continue
            full_name2 = input("Enter the second contact's full name: ").strip()
            if full_name2.lower() == "cancel":
                print("Merge operation canceled. Returning to the main menu.")
                continue

            phonebook.merge_contacts(full_name1, full_name2)

        elif choice == '9':  # Filter Contacts by Date
            print("\n** Type 'cancel' at any time to stop filtering and return to the main menu **")
            
            while True:
                start_date = input("Enter start date (YYYY-MM-DD): ").strip()
                if start_date.lower() == "cancel":
                    print("Filter operation canceled. Returning to the main menu.")
                    break
                
                end_date = input("Enter end date (YYYY-MM-DD): ").strip()
                if end_date.lower() == "cancel":
                    print("Filter operation canceled. Returning to the main menu.")
                    break
                
                try:
                    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

                    if end_date_obj < start_date_obj:
                        print("End date cannot be earlier than start date. Please enter the dates again.")
                        continue  # Ask for the dates again
                    break  # Exit the loop if dates are valid
                except ValueError:
                    print("Invalid date format. Please use 'YYYY-MM-DD'.")
                    continue  # Ask for the dates again
            
            if start_date.lower() != "cancel" and end_date.lower() != "cancel":
                phonebook.filter_contacts_by_date(start_date, end_date)

        elif choice == '10':  # Exit
            print("Exiting the phone book.")
            break

        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
