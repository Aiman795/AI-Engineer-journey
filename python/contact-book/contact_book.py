import json
import logging
from dataclasses import dataclass, asdict
from pathlib import Path


# TODO: logging config

#  Contact dataclass
@dataclass
class Contact:
    name:str
    phone:str
    email:str=""

# custom exceptions
class ContactBookError(Exception):
    "contact book errors"
class ContactNotFoundError(ContactBookError):
    "Contact not found"
class DuplicateContactError(ContactBookError):
    "Duplicate contacts"


class ContactBook:
    def __init__(self):
        self.contacts = []                      # one list of Contact objects

    def _find(self, name):
        """Return the Contact with this name (ignoring case), or None."""
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def add(self, contact):
        if self._find(contact.name) is not None:
            raise DuplicateContactError(f"{contact.name} already exists")
        self.contacts.append(contact)           # only store after the check passes

    def list_all(self):
        return self.contacts                    # return the list stored on the object

    def search(self, text):
        return [
            contact for contact in self.contacts
            if text.lower() in contact.name.lower()
        ]                                       # always a list, empty if no match

    def delete(self, name):
        contact = self._find(name)
        if contact is None:
            raise ContactNotFoundError(f"No contact named {name}")
        self.contacts.remove(contact)           # remove only after validating
# # contact class
# class ContactBook:
#     def __init__(self):
#         self.contacts = []

#     def add(self, contact):
#         for contact in self.contacts:
#             if contact.name in self.contacts:
#                 raise DuplicateContactError("Already present")

#     def list_all(self):
#         ...   # return the list of contacts
#         return self.contacts

#     def search(self, text):
#         ...   # contacts whose name contains text, ignoring case
#         if text in self.contacts:
#             return self.names

#     def delete(self, name):
#         if name not in self.names:
#             raise ContactNotFoundError("Not present")

def main():
    book = ContactBook()
    book.add(Contact("Ali", "0300"))
    book.add(Contact("Sara", "0311", "sara@example.com"))
    
    print(book.list_all())           # both contacts
    print(book.search("al"))         # [Contact(name='Ali', phone='0300', email='')]
    print(book.search("zzz"))        # []
    
    try:
        book.add(Contact("ali", "0999"))
    except DuplicateContactError as e:
        print("Error:", e)           # ali already exists
    
    book.delete("Sara")
    print(len(book.list_all()))      # 1
    
    try:
        book.delete("Nobody")
    except ContactNotFoundError as e:
        print("Error:", e)           # No contact named Nobody

if __name__ == "__main__":
    main()
