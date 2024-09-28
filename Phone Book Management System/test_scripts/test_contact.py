import unittest
import sys
import os

# Add the directory containing the modules to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from contact import Contact

class TestContact(unittest.TestCase):
    
    def test_contact_initialization(self):
        """Test the initialization of the Contact class."""
        contact = Contact(
            first_name="John",
            last_name="Doe",
            phone_numbers=["(123) 456-7890"],
            email="john.doe@example.com",
            address="123 Main St"
        )
        self.assertEqual(contact.first_name, "John")
        self.assertEqual(contact.last_name, "Doe")
        self.assertEqual(contact.phone_numbers, ["(123) 456-7890"])
        self.assertEqual(contact.email, "john.doe@example.com")
        self.assertEqual(contact.address, "123 Main St")
        self.assertIsNotNone(contact.created_at)

    def test_update_contact(self):
        """Test updating the Contact details."""
        contact = Contact("Jane", "Doe", ["(987) 654-3210"])
        contact.update_contact(phone_numbers=["(111) 222-3333"], email="jane.doe@example.com")
        self.assertEqual(contact.phone_numbers, ["(111) 222-3333"])
        self.assertEqual(contact.email, "jane.doe@example.com")
        self.assertIsNotNone(contact.updated_at)

if __name__ == "__main__":
    unittest.main()
