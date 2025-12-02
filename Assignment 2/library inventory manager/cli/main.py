import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

inventory = LibraryInventory()

def menu():
    while True:
        print("\n========== Library Menu ==========")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.is_available():
                book.issue()
                inventory.save_books()
                print("Book issued!")
            else:
                print("Book not available!")

        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_books()
                print("Book returned!")
            else:
                print("Book not found!")

        elif choice == 4:
            for b in inventory.display_all():
                print(b)

        elif choice == 5:
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No book found!")

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid menu option!")

if __name__ == "__main__":
    menu()
