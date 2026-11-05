class Book:
 #Book class
#Attributes: title, author, isbn, year
#Class variable total_books that increases every time a Book is created
    total_books = 0
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn       # goes through the setter, so it gets validated
        self.year = year
        Book.total_books += 1
#isbn is a @property with a setter that raises ValueError unless it is exactly 13 digits
    @property
    def isbn(self):
        return self._isbn         # getter just returns the stored value

    @isbn.setter
    def isbn(self, value):
        if not Book.is_valid_isbn(value):
            raise ValueError("ISBN must be exactly 13 digits")
        else:
            self._isbn = value      # stored under a different name to avoid infinite recursion

#@staticmethod is_valid_isbn(isbn) that does the check, which the setter reuses
    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()
#@classmethod from_string(cls, text) that builds a book from "Title|Author|ISBN|Year"
    @classmethod
    def from_string(cls, text):
        title, author, isbn, year = text.split("|")
        return cls(title, author, isbn, int(year))
#__str__ (readable), __repr__ (debug-friendly), __eq__ (two books are equal if their ISBNs match), and __lt__ (sort by title)
    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}, Year: {self.year})"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r}, {self.year!r})"

    def __eq__(self, other):
        return self.isbn == other.isbn

    def __lt__(self, other):
        return self.title < other.title


#Member class
class Member:
  #Member has name, a borrowed list, and class variable max_books = 3
  max_books = 3
  def __init__(self, name):
        self.name = name
        self.borrowed = []
#__len__ returns how many books the member has borrowed
  def __len__(self):
    return len(self.borrowed)
#PremiumMember(Member) overrides max_books = 10
class PremiumMember(Member):
    max_books = 10
    
from dataclasses import dataclass,field
from datetime import date,timedelta
@dataclass
class Loan:
  book:Book
  member_name:str
  due_date:date=field(default_factory=lambda: date.today() + timedelta(days=14))
  def is_overdue(self):
    # return True if today is later than due_date
    if date.today() > self.due_date:
      return True
    else:
      return False

class Library:
  def __init__(self):
    self.books={}
    self.loans={}
  def add_book(self, book):
    if book.isbn in self.books:
      raise ValueError("already present")
    else:
      self.books[book.isbn] = book
  
  def __contains__(self, isbn):
      if isbn in self.books:
        return True
      else:
        return False

  def __iter__(self):
        return iter(self.books.values())

  def borrow(self, isbn, member):
    # 1. not found -> ValueError
    if isbn not in self.books:
      raise ValueError("Book not found")
    # 2. already borrowed -> ValueError
    elif isbn in self.loans:
      raise ValueError("Book already borrowed")
    # 3. over limit -> ValueError
    elif len(member) >= member.max_books:
      raise ValueError("Over limit")
    # then: create Loan, store it, append to member.borrowed
    else:
      book= self.books[isbn]
      self.loans[isbn] = Loan(book, member.name)
      member.borrowed.append(book)


  def return_book(self, isbn, member):
      # 1. not on loan -> ValueError
    if isbn not in self.loans:
      raise ValueError("Book not borrowed")
    # then: delete loan, remove from member.borrowed
    else:
      book=self.books[isbn]
      if book not in member.borrowed:
        raise ValueError("This member did not borrow this book")
      del self.loans[isbn]
      member.borrowed.remove(book)
      
  
    
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Dune", "Frank Herbert", "9780441172719", 1965))
    alice = Member("Alice")
    bob = PremiumMember("Bob")

    lib.borrow("9780441172719", alice)

    try:
        lib.return_book("9780441172719", bob)      # wrong member
    except ValueError as e:
        print("Error:", e)
    print(lib.loans)                               # loan must STILL be there

    lib.return_book("9780441172719", alice)        # correct member
    print(lib.loans)                               # {}
    print(len(alice))        
    b1 = Book("Dune", "Frank Herbert", "9780441172719", 1965)
    
    old = Loan(b1, "Alice", due_date=date(2020, 1, 1))
    print(old.is_overdue())                  # True
    print(Loan(b1, "Alice").is_overdue())    # False