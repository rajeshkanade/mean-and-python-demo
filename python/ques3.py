class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book borrowed successfully!")
        else:
            print("Sorry, no copies available.")
    
    def return_book(self):
        self.copies += 1
        print("Book returned successfully!")
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies Available: {self.copies}")


# --- Main program ---
title = input("Enter book title: ")
author = input("Enter author name: ")
copies = int(input("Enter number of copies: "))

book = Book(title, author, copies)

print("\nBook Information:")
book.display_info()

# Borrow or return
choice = input("\nDo you want to borrow or return the book? (borrow/return): ").strip().lower()

if choice == "borrow":
    book.borrow_book()
elif choice == "return":
    book.return_book()
else:
    print("Invalid choice.")

print("\nUpdated Book Information:")
book.display_info()
