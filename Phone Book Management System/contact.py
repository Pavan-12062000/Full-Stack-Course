from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone_numbers, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers if isinstance(phone_numbers, list) else [phone_numbers]
        self.email = email
        self.address = address
        self.created_at = datetime.now()
        self.updated_at = None  # Initialize as None to represent no updates

    def update_contact(self, first_name=None, last_name=None, phone_numbers=None, email=None, address=None):
        """Update the contact details."""
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if phone_numbers:
            self.phone_numbers = phone_numbers if isinstance(phone_numbers, list) else [phone_numbers]
        if email:
            self.email = email
        if address:
            self.address = address

        self.updated_at = datetime.now()  # Set the updated_at when the contact is modified

    def merge_contact(self, other_contact):
        """Merge another contact into this one."""
        # Add phone numbers, avoiding duplicates
        for phone in other_contact.phone_numbers:
            if phone not in self.phone_numbers:
                self.phone_numbers.append(phone)
        
        # Combine email addresses if both are present
        if self.email and other_contact.email and self.email != other_contact.email:
            self.email = f"{self.email}, {other_contact.email}"
        elif not self.email:
            self.email = other_contact.email
        
        # Combine addresses if both are present
        if self.address and other_contact.address and self.address != other_contact.address:
            self.address = f"{self.address}, {other_contact.address}"
        elif not self.address:
            self.address = other_contact.address
        
        # Update the updated_at timestamp
        self.updated_at = datetime.now()


    def __str__(self):
        # Join all phone numbers into a single string
        phone_numbers_str = ', '.join(self.phone_numbers)

        contact_details = (
            f"Name: {self.first_name} {self.last_name}, "
            f"Phone: {phone_numbers_str}, "
            f"Email: {self.email if self.email else 'N/A'}, "
            f"Address: {self.address if self.address else 'N/A'}, "
            f"Created At: {self.created_at}"
        )
        
        # Show 'updated_at' only if the contact has been updated
        if self.updated_at:
            contact_details += f", Updated At: {self.updated_at}"
        
        return contact_details
