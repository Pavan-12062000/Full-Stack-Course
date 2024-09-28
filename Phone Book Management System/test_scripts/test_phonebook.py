import unittest
import sys
import os

# Add the directory containing the modules to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phonebook import PhoneBook
from contact import Contact

class TestPhoneBook(unittest.TestCase):

    def test_add_contact(self):
        """Test adding a contact to PhoneBook."""
        phonebook = PhoneBook()
        contact = Contact("Alice", "Smith", ["(555) 123-4567"], "alice.smith@example.com", "456 Elm St")
        phonebook.add_contact(contact)
        self.assertEqual(len(phonebook.contacts), 1)
        self.assertEqual(phonebook.contacts[0].first_name, "Alice")

    def test_delete_contact(self):
        """Test deleting a contact from PhoneBook."""
        phonebook = PhoneBook()
        contact = Contact("Bob", "Johnson", ["(555) 234-5678"])
        phonebook.add_contact(contact)
        phonebook.delete_contact("Bob Johnson")
        self.assertEqual(len(phonebook.contacts), 0)

    def test_import_export_contacts(self):
        """Test importing and exporting contacts."""
        phonebook = PhoneBook()
        contact = Contact("Charlie", "Brown", ["(555) 345-6789"])
        phonebook.add_contact(contact)

        # Export contacts to a CSV file
        phonebook.export_contacts_to_csv("contacts.csv")

        # Create a new PhoneBook and import contacts from CSV
        new_phonebook = PhoneBook()
        new_phonebook.import_contacts_from_csv("contacts.csv")
        self.assertEqual(len(new_phonebook.contacts), 1)
        self.assertEqual(new_phonebook.contacts[0].first_name, "Charlie")


if __name__ == "__main__":
    unittest.main()
