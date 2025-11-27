from typing import List, Optional
import json

# ==========================
# CLASS BOOK
# ==========================
class Book:
    """
    Represents a book in the library.

    Attributes:
        title       - book title
        author      - author name
        year        - publication year
        category    - book category/genre
        available   - True if available for borrowing, False if borrowed
    """

    def __init__(self, title: str, author: str, year: int,
                 category: str = "General", available: bool = True) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.available = available

    def describe(self) -> None:
        """Prints a simple description of the book."""
        print(f"'{self.title}' by {self.author} (Year {self.year})")

    def mark_borrowed(self) -> bool:
        """Marks the book as borrowed if available."""
        if self.available:
            self.available = False
            print(f"Book '{self.title}' has been borrowed.")
            return True
        print(f"Book '{self.title}' is already borrowed.")
        return False

    def mark_returned(self) -> bool:
        """Marks the book as returned if it was borrowed."""
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' has been returned.")
            return True
        print(f"Book '{self.title}' was already available.")
        return False

    def __str__(self) -> str:
        status = "available" if self.available else "borrowed"
        return f"{self.title} – {self.author} – {status}"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "category": self.category,
            "available": self.available
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            category=data.get("category", "General"),
            available=data.get("available", True)
        )

# ==========================
# CLASS READER
# ==========================
class Reader:
    """
    Represents a library reader.

    Attributes:
        name         - reader's name
        email        - reader's email
        borrowed_books - list of Book objects currently borrowed
    """

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.borrowed_books: List[Book] = []

    def borrow_book(self, book: Book) -> bool:
        """Attempts to borrow a book. Returns True if successful."""
        if book.mark_borrowed():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
            return True
        print(f"{self.name} could not borrow '{book.title}'.")
        return False

    def return_book(self, book: Book) -> bool:
        """Attempts to return a book. Returns True if successful."""
        if book in self.borrowed_books and book.mark_returned():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
            return True
        print(f"{self.name} does not have '{book.title}'.")
        return False

    def list_books(self) -> None:
        """Prints the list of books currently borrowed by the reader."""
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed the following books:")
            for b in self.borrowed_books:
                print(f" - {b.title}")

    def __str__(self) -> str:
        return f"{self.name} has {len(self.borrowed_books)} borrowed books"

# ==========================
# CLASS LIBRARY
# ==========================
class Library:
    """
    Represents a library managing a collection of books.

    Attributes:
        name                   - library name
        books                  - list of Book objects
        total_successful_borrows - total number of successful borrows
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.books: List[Book] = []
        self.total_successful_borrows: int = 0

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def display_books(self) -> None:
        """Prints all books in the library."""
        print(f"\nBooks in {self.name}:")
        if not self.books:
            print(" - No books available.")
        else:
            for b in self.books:
                print(f" - {b}")

    def _find_book_by_title(self, title: str) -> Optional[Book]:
        """Internal helper to find a book by title (case-insensitive)."""
        t = title.strip().lower()
        for b in self.books:
            if b.title.strip().lower() == t:
                return b
        return None

    def search_by_author(self, author: str) -> List[Book]:
        """Searches for books by author (case-insensitive)."""
        author_norm = author.strip().lower()
        found = [b for b in self.books if b.author.strip().lower() == author_norm]

        print(f"\nSearching for books by: {author}")
        if not found:
            print(" - No books found.")
        else:
            for b in found:
                print(f" - {b}")
        return found

    def borrow_book(self, reader: Reader, title: str) -> bool:
        """Allows a reader to borrow a book by title."""
        book = self._find_book_by_title(title)
        if book and book.available:
            if reader.borrow_book(book):
                self.total_successful_borrows += 1
                return True
        print(f"Book '{title}' is not available or does not exist.")
        return False

    def return_book(self, reader: Reader, title: str) -> bool:
        """Allows a reader to return a book by title."""
        book = self._find_book_by_title(title)
        if book:
            return reader.return_book(book)
        print(f"Book '{title}' was not found in the library.")
        return False

    def search_by_year(self, year: int) -> List[Book]:
        """Searches for books by publication year."""
        found = [b for b in self.books if b.year == year]
        print(f"\nSearching for books published in {year}:")
        if not found:
            print(" - No books found.")
        else:
            for b in found:
                print(f" - {b}")
        return found

    def display_books_sorted_by_year(self) -> None:
        """Displays books sorted by publication year."""
        unique_years = sorted({b.year for b in self.books})
        print("\nBooks sorted by publication year:")
        for year in unique_years:
            self.search_by_year(year)

    def available_books(self) -> List[Book]:
        """Returns all available books."""
        available = [b for b in self.books if b.available]
        print("\nAvailable books:")
        if not available:
            print(" - No books available.")
        else:
            for b in available:
                print(f" - {b}")
        return available

    def save_to_file(self, filename: str) -> None:
        """Saves the library books to a JSON file."""
        data = [b.to_dict() for b in self.books]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Library data saved to '{filename}'!")

    def load_from_file(self, filename: str) -> None:
        """Loads library books from a JSON file."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.books = [Book.from_dict(d) for d in data]
            print(f"Loaded {len(self.books)} books from '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty library.")
            self.books = []
        except json.JSONDecodeError:
            print(f"File '{filename}' is not valid JSON.")
            self.books = []

    def report_statistics(self) -> None:
        """Prints a summary report of the library."""
        total = len(self.books)
        available_count = sum(1 for b in self.books if b.available)
        borrowed_count = total - available_count
        print("\n==== LIBRARY REPORT ====")
        print(f"Name: {self.name}")
        print(f"Total books: {total}")
        print(f"Available books: {available_count}")
        print(f"Borrowed books: {borrowed_count}")
        print(f"Total successful borrows: {self.total_successful_borrows}")

# ==========================
# DEMO / MAIN
# ==========================
def main():
    library = Library("Central Library")
    reader = Reader("Ana Pop", "ana@example.com")

    library.add_book(Book("The Little Prince", "Antoine de Saint-Exupéry", 1943, category="Fiction"))
    library.add_book(Book("Ion", "Liviu Rebreanu", 1920, category="Classic"))
    library.add_book(Book("Baltagul", "Mihail Sadoveanu", 1930, category="Classic"))

    library.display_books()
    library.report_statistics()

    while True:
        print("""
## ********* LIBRARY MENU *********

1. Display all books
2. Display books sorted by year
3. Add a book
4. Search by author
5. Search by publication year
6. Borrow a book
7. Return a book
8. Library report
9. Save library to JSON
10. Load library from JSON
0. Exit
""")
        option = input("Choose an option: ").strip()

        if option == '1':
            library.display_books()
        elif option == '2':
            library.display_books_sorted_by_year()
        elif option == '3':
            print("\n--- Add a Book ---")
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            try:
                year = int(input("Publication year: ").strip())
            except ValueError:
                print("Invalid year. Book was not added.")
                continue
            category = input("Category (e.g., Fiction, Classic): ").strip() or "General"
            library.add_book(Book(title, author, year, category))
        elif option == '4':
            author = input("Author name: ").strip()
            library.search_by_author(author)
        elif option == '5':
            try:
                year = int(input("Publication year: ").strip())
                found = library.search_by_year(year)
                if not found:
                    print("\nNo books found for this year. Available books:")
                    for b in library.books:
                        print(f" - {b.title} ({b.year})")
            except ValueError:
                print("Invalid year. Must be an integer.")
        elif option == '6':
            title = input("Book title to borrow: ").strip()
            if library.borrow_book(reader, title):
                print(f"Borrow successful for {reader.name}.")
            reader.list_books()
        elif option == '7':
            title = input("Book title to return: ").strip()
            if library.return_book(reader, title):
                print(f"Return successful for {reader.name}.")
            reader.list_books()
        elif option == '8':
            library.report_statistics()
        elif option == '9':
            filename = "library_data.json"
            library.save_to_file(filename)
        elif option == '10':
            filename = "library_data.json"
            library.load_from_file(filename)
        elif option == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication stopped manually. Goodbye!")
1