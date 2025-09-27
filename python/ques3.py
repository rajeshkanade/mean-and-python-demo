# A library system needs a Book class with the attributes title, author, copies_available.
# Implement methods:
# - borrow_book() (decrease copy count if available)
# - return_book() (increase copy count)
# - display_info()

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False
    
    def return_book(self):
        self.copies += 1
    
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

# Example usage
book = Book("Python Basics", "John Doe", 5)
print(book.display_info())
book.borrow_book()
print(book.display_info())
book.return_book()
print(book.display_info())