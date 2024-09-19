from datetime import datetime
import logging
import csv
from contact import Contact

class PhoneBook:
    def __init__(self):
        self.contacts = []
        logging.basicConfig(
            filename="logs/phonebook.log", level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def add_contact(self, contact):
        """Add a new contact to the phonebook."""
        self.contacts.append(contact)
        logging.info(
            f"Added new contact: {contact.first_name} {contact.last_name} | "
            f"Phone: {', '.join(contact.phone_numbers)}, Email: {contact.email}, Address: {contact.address} | "
            f"Created At: {contact.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    def find_contact(self, search_term):
        """Find contacts using full name or partial name matching, case-insensitive, and phone number."""
        search_results = []
        search_term_lower = search_term.lower()

        for contact in self.contacts:
            full_name = f"{contact.first_name} {contact.last_name}"
            full_name_lower = full_name.lower()
            
            # Check if the search term matches the full name or any phone number
            if (search_term_lower in full_name_lower or
                any(search_term_lower in phone.lower() for phone in contact.phone_numbers)):
                search_results.append(contact)

        return search_results


    def delete_contact(self, search_term):
        """Delete a contact from the phonebook with two-step confirmation."""
        results = self.find_contact(search_term)
        if results:
            # Show the contact that is going to be deleted
            print("\nThe below contact is getting deleted:")
            for contact in results:
                print(contact)
            
            # Ask for confirmation
            confirmation = input("Are you sure you want to delete the contact (y/n): ").strip().lower()
            if confirmation == 'y':
                for contact in results:
                    self.contacts.remove(contact)
                    logging.info(
                        f"Deleted contact: {contact.first_name} {contact.last_name} | "
                        f"Phone: {', '.join(contact.phone_numbers)}, Email: {contact.email}, Address: {contact.address}"
                    )
                print("Contact deleted successfully.")
                return True
            elif confirmation == 'n':
                print("Delete operation canceled. Returning to the main menu.")
                return False
            else:
                print("Invalid input. Operation canceled. Returning to the main menu.")
                return False
        else:
            print("Contact not found.")
            return False


    def update_contact(self, search_term, first_name=None, last_name=None,
                       phone_numbers=None, email=None, address=None):
        """Update a contact's details."""
        results = self.find_contact(search_term)
        if results:
            for contact in results:
                old_details = str(contact)
                contact.update_contact(first_name, last_name, phone_numbers, email, address)
                logging.info(
                    f"Updated contact: {old_details} | "
                    f"Updated At: {contact.updated_at.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            return True
        return False

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        for contact in self.contacts:
            print(contact)
            print("\n")  # Blank line between contacts

    def export_contacts_to_csv(self, csv_file_path):
        """Export contacts to a CSV file."""
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Writing header row
            writer.writerow(["First Name", "Last Name", "Phone Numbers", "Email", "Address", "Created At", "Updated At"])

            # Write each contact as a row in the CSV
            for contact in self.contacts:
                writer.writerow([
                    contact.first_name,
                    contact.last_name,
                    ", ".join(contact.phone_numbers),
                    contact.email if contact.email else "",  # Handle empty email
                    contact.address if contact.address else "",  # Handle empty address
                    contact.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format Created At timestamp
                    contact.updated_at.strftime('%Y-%m-%d %H:%M:%S') if contact.updated_at else ""  # Only add updated_at if present
                ])
        print(f"Contacts successfully exported to {csv_file_path}.")

    def import_contacts_from_csv(self, csv_file_path):
        """Import contacts from a CSV file."""
        try:
            with open(csv_file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact = Contact(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        phone_numbers=row['Phone Numbers'].split(", "),
                        email=row.get('Email'),
                        address=row.get('Address')
                    )
                    self.add_contact(contact)
            logging.info(f"Imported contacts from {csv_file_path}")
            print(f"Contacts imported successfully from {csv_file_path}")
        except FileNotFoundError:
            print(f"File '{csv_file_path}' not found.")
        except KeyError:
            print("CSV file is missing one or more required columns: 'First Name', 'Last Name', 'Phone Numbers'.")
        except Exception as e:
            print(f"An error occurred while importing: {e}")

    def merge_contacts(self, full_name1, full_name2):
        """Merge two contacts by their full names."""
        contact1 = self.find_contact(full_name1)
        contact2 = self.find_contact(full_name2)

        if contact1 and contact2:
            # Merge the first contact with the second contact
            contact1[0].merge_contact(contact2[0])
            # Remove the second contact from the list
            self.contacts.remove(contact2[0])
            print(f"Contacts merged successfully. Resulting contact:\n{contact1[0]}")
            logging.info(f"Merged contacts: {full_name1} and {full_name2}")
        else:
            print("One or both contacts not found.")

    def filter_contacts_by_date(self, start_date_str, end_date_str):
        """Filter contacts based on a date range."""
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
            return

        filtered_contacts = [
            contact for contact in self.contacts
            if (contact.created_at >= start_date and contact.created_at <= end_date) or
               (contact.updated_at and contact.updated_at >= start_date and contact.updated_at <= end_date)
        ]

        if filtered_contacts:
            for contact in filtered_contacts:
                print(contact)
                print("\n")  # Blank line between contacts
        else:
            print("No contacts found in the specified date range.")