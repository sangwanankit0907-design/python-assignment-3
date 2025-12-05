import sys
import os

# Add project root to sys.path so Python can find library_manager
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from library_manager.inventory import LibraryInventory
from library_manager.book import Book

library = LibraryInventory()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")

        book = Book(title, author, isbn)
        library.add_book(book)
        print("Book added successfully")

    elif choice == "2":
        isbn = input("Enter ISBN to issue: ")
        book = library.search_by_isbn(isbn)
        if book:
            if book.issue():
                library.save_books()
                print("Book issued successfully")
            else:
                print("Book already issued")
        else:
            print("Book not found")

    elif choice == "3":
        isbn = input("Enter ISBN to return: ")
        book = library.search_by_isbn(isbn)
        if book:
            book.return_book()
            library.save_books()
            print("Book returned successfully")
        else:
            print("Book not found")

    elif choice == "4":
        library.display_all()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")