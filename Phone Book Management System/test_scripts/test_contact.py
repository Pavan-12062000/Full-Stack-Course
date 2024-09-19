import sys
import os

# Add the directory containing the modules to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from contact import Contact

def test_contact_initialization():
    """Test the initialization of the Contact class."""
    contact = Contact(
        first_name="John",
        last_name="Doe",
        phone_numbers=["(123) 456-7890"],
        email="john.doe@example.com",
        address="123 Main St"
    )
    assert contact.first_name == "John"
    assert contact.last_name == "Doe"
    assert contact.phone_numbers == ["(123) 456-7890"]
    assert contact.email == "john.doe@example.com"
    assert contact.address == "123 Main St"
    assert contact.created_at is not None

def test_update_contact():
    """Test updating the Contact details."""
    contact = Contact("Jane", "Doe", ["(987) 654-3210"])
    contact.update_contact(phone_numbers=["(111) 222-3333"], email="jane.doe@example.com")
    assert contact.phone_numbers == ["(111) 222-3333"]
    assert contact.email == "jane.doe@example.com"
    assert contact.updated_at is not None

if __name__ == "__main__":
    test_contact_initialization()
    test_update_contact()
    print("All tests passed!")
