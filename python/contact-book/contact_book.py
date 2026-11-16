import json
import logging
from dataclasses import dataclass, asdict
from pathlib import Path

import os
from dotenv import load_dotenv

load_dotenv()
DATA_FILE = os.getenv("DATA_FILE", "contacts.json")

# logging config
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

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
        logging.info(f"Added contact: {contact.name}")

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
        logging.info(f"Deleted contact: {contact.name}")

    def save(self, path):
        data = [asdict(contact) for contact in self.contacts]
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, path):
        path = Path(path)
        if not path.exists():                 # first run: no file yet
            self.contacts = []
            logging.warning(f"{path} not found, starting empty")
            return
            

        try:
            with open(path, "r") as f:
                data = json.load(f)           # a list of dictionaries
        except json.JSONDecodeError as e:
            logging.exception(f"Could not read {path}: invalid JSON ({e})")
            self.contacts = []
            return
            

        self.contacts = []
        for d in data:
            try:
                self.contacts.append(Contact(**d))
            except TypeError:
                logging.warning(f"Skipping invalid entry: {d}")

        logging.info(f"Loaded {len(self.contacts)} contacts from {path}")

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



def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Quit")


def main():
    book = ContactBook()
    book.load(DATA_FILE)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email (optional): ").strip()

            if not name or not phone:
                print("Name and phone are required.")
                continue

            try:
                book.add(Contact(name, phone, email))
                book.save(DATA_FILE)
                print(f"Added {name}.")
            except ContactBookError as e:
                print("Error:", e)

        elif choice == "2":
            contacts = book.list_all()
            if not contacts:
                print("No contacts yet.")
            else:
                for c in contacts:
                    print(f"{c.name} | {c.phone} | {c.email or '-'}")

        elif choice == "3":
            text = input("Search for: ").strip()
            matches = book.search(text)
            if not matches:
                print("No matches found.")
            else:
                for c in matches:
                    print(f"{c.name} | {c.phone} | {c.email or '-'}")

        elif choice == "4":
            name = input("Name to delete: ").strip()
            try:
                book.delete(name)
                book.save(DATA_FILE)
                print(f"Deleted {name}.")
            except ContactBookError as e:
                print("Error:", e)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, enter a number from 1 to 5.")


if __name__ == "__main__":
    main()