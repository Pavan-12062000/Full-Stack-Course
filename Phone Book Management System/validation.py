import re


def validate_phone_number(phone_number):
    """Validate phone number format (###) ###-####."""
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    return bool(pattern.match(phone_number))


def validate_email(email):
    """Validate email format."""
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))


def validate_input(prompt, validation_func, error_message="Invalid input."):
    """Prompt user for input and validate it."""
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print(error_message)
