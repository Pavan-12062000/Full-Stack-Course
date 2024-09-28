import unittest
from validation import validate_phone_number, validate_email

class TestValidation(unittest.TestCase):

    def test_validate_phone_number(self):
        """Test phone number validation."""
        self.assertTrue(validate_phone_number("(123) 456-7890"))
        self.assertFalse(validate_phone_number("(123) 456-789"))  # Invalid format
        self.assertFalse(validate_phone_number("123-456-7890"))  # Invalid format

    def test_validate_email(self):
        """Test email validation."""
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("test.email+alex@leetcode.com"))
        self.assertFalse(validate_email("test@example"))  # Missing domain
        self.assertFalse(validate_email("test.com"))  # Missing '@'

if __name__ == '__main__':
    unittest.main()
