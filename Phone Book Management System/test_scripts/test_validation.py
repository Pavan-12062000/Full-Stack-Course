import sys
import os

# Add the directory containing the modules to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validation import validate_phone_number, validate_email

def test_validate_phone_number():
    """Test the validate_phone_number function."""
    assert validate_phone_number("(123) 456-7890") == True
    assert validate_phone_number("123-456-7890") == False
    assert validate_phone_number("(123) 456-789") == False
    assert validate_phone_number("(123) 456-78900") == False

def test_validate_email():
    """Test the validate_email function."""
    assert validate_email("test@example.com") == True
    assert validate_email("test.example.com") == False
    assert validate_email("test@.com") == False
    assert validate_email("test@com") == False

if __name__ == "__main__":
    test_validate_phone_number()
    test_validate_email()
    print("All tests passed!")
