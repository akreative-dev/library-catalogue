
import uuid
from datetime import datetime, timedelta


class Book:
    """Represent a book held in the library catalogue."""

    def __init__(
        self, ID, title, author, publisher, year, no_copies, publication_year
    ):
        if not title or not title.strip():
            raise ValueError("Book title cannot be empty.")
        if not author or not author.strip():
            raise ValueError("Book author cannot be empty.")
        if int(no_copies) < 0:
            raise ValueError("Number of copies cannot be negative.")

        # IDs are generated automatically rather than supplied by callers.
        self.ID = uuid.uuid4()
        self.title = title.strip()
        self.author = author.strip()
        self.publisher = publisher
        self.year = year
        self.no_copies = int(no_copies)
        self.publication_year = publication_year
        self.borrowed_copies = 0

    def __str__(self):
        return (
            f"{self.title} by {self.author} ({self.publisher}, {self.year}, "
            f"published in {self.publication_year}) - "
            f"total copies: {self.no_copies}, "
            f"available: {self.get_available_copies()}"
        )

    def info(self):
        return f"{self.title}, ID: {self.ID}"

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_year(self):
        return self.year

    def get_total_copies(self):
        return self.no_copies

    def get_available_copies(self):
        return self.no_copies - self.borrowed_copies

    def set_title(self, new_title):
        if not new_title or not new_title.strip():
            raise ValueError("Book title cannot be empty.")
        self.title = new_title.strip()

    def set_author(self, author):
        if not author or not author.strip():
            raise ValueError("Book author cannot be empty.")
        self.author = author.strip()

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_year(self, year):
        self.year = year

    def set_no_copies(self, no_copies):
        no_copies = int(no_copies)
        if no_copies < self.borrowed_copies:
            raise ValueError(
                "Total copies cannot be fewer than the copies currently on loan."
            )
        if no_copies < 0:
            raise ValueError("Number of copies cannot be negative.")
        self.no_copies = no_copies

    def set_publication_year(self, publication_year):
        self.publication_year = publication_year


class Book_list:
    """Manage the library's book catalogue."""

    def __init__(self):
        self.book_list = []
        self.available_books = {}

    def __str__(self):
        return f"Book catalogue ({len(self.book_list)} titles)"

    def print_book_list(self):
        for book in self.book_list:
            print(book)

    def print_available_books(self):
        for book in self.book_list:
            if book.get_available_copies() > 0:
                print(book)

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")

        for existing in self.book_list:
            if (
                existing.title.casefold() == book.title.casefold()
                and existing.author.casefold() == book.author.casefold()
            ):
                raise ValueError(
                    "This title and author already exist. "
                    "Use increase_copies() to add copies."
                )

        self.book_list.append(book)
        self.available_books[book.ID] = book.get_available_copies()
        return book

    def increase_copies(self, title, author, quantity=1):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 1:
            raise ValueError("Quantity must be a positive integer.")

        for book in self.book_list:
            if (
                book.title.casefold() == title.casefold()
                and book.author.casefold() == author.casefold()
            ):
                book.set_no_copies(book.no_copies + quantity)
                self.available_books[book.ID] = book.get_available_copies()
                return book

        raise ValueError("Book not found in the catalogue.")

    def remove_book(self, title):
        for book in self.book_list:
            if book.title.casefold() == title.casefold():
                if book.borrowed_copies:
                    raise ValueError("Cannot remove a book while copies are on loan.")
                self.book_list.remove(book)
                self.available_books.pop(book.ID, None)
                return book
        raise ValueError("Book not found in the catalogue.")

    def search_book_title(self, title):
        return [
            book for book in self.book_list
            if book.title.casefold() == title.casefold()
        ]

    def search_book_author(self, author):
        return [
            book for book in self.book_list
            if book.author.casefold() == author.casefold()
        ]

    def search_book_publisher(self, publisher):
        return [
            book for book in self.book_list
            if (book.publisher or "").casefold() == publisher.casefold()
        ]

    def search_book_publication_year(self, publication_year):
        return [
            book for book in self.book_list
            if str(book.publication_year) == str(publication_year)
        ]

    def get_total_copies(self):
        return sum(book.get_total_copies() for book in self.book_list)


class User:
    """Represent a registered library user."""

    def __init__(
        self, user_name, first_name, surname,
        house_no="", road="", postcode="", email="", DOB=""
    ):
        if not user_name or not user_name.strip():
            raise ValueError("Username cannot be empty.")
        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty.")
        if not surname or not surname.strip():
            raise ValueError("Surname cannot be empty.")

        self.user_name = user_name.strip()
        self.first_name = first_name.strip()
        self.surname = surname.strip()
        self.house_no = house_no
        self.road = road
        self.postcode = postcode
        self.email = email
        self.DOB = DOB

    def __str__(self):
        # Avoid exposing private contact details in general output.
        return f"{self.user_name} — {self.first_name} {self.surname}"

    def get_user_name(self):
        return self.user_name

    def get_first_name(self):
        return self.first_name

    def get_surname(self):
        return self.surname

    def get_house_no(self):
        return self.house_no

    def get_road(self):
        return self.road

    def get_postcode(self):
        return self.postcode

    def get_email(self):
        return self.email

    def get_DOB(self):
        return self.DOB

    def set_user_name(self, user_name):
        if not user_name or not user_name.strip():
            raise ValueError("Username cannot be empty.")
        self.user_name = user_name.strip()

    def set_first_name(self, first_name):
        if not first_name or not first_name.strip():
            raise ValueError("First name cannot be empty.")
        self.first_name = first_name.strip()

    def set_surname(self, surname):
        if not surname or not surname.strip():
            raise ValueError("Surname cannot be empty.")
        self.surname = surname.strip()

    def set_house_no(self, house_no):
        self.house_no = house_no

    def set_road(self, road):
        self.road = road

    def set_postcode(self, postcode):
        self.postcode = postcode

    def set_email(self, email):
        self.email = email

    def set_DOB(self, DOB):
        self.DOB = DOB


class User_list:
    """Manage registered library users."""

    def __init__(self):
        self.user_list = []

    def __str__(self):
        return f"Registered users: {len(self.user_list)}"

    def add_user(self, user):
        if not isinstance(user, User):
            raise TypeError("Only User instances can be added.")

        if any(
            existing.user_name.casefold() == user.user_name.casefold()
            for existing in self.user_list
        ):
            raise ValueError("A user with this username already exists.")

        self.user_list.append(user)
        return user

    def remove_user(self, user_name):
        """Remove a user by their unique username."""
        for user in self.user_list:
            if user.user_name.casefold() == user_name.casefold():
                self.user_list.remove(user)
                return user
        raise ValueError("User not found.")

    def count_users(self):
        return len(self.user_list)

    def get_user_details(self, user_name):
        """Return the matching user, or None if not found."""
        for user in self.user_list:
            if user.user_name.casefold() == user_name.casefold():
                return user
        return None







class Loans:
    """Manage book loans, returns and due dates."""

    LOAN_PERIOD_DAYS = 30

    def __init__(self, catalogue, users):
        self.catalogue = catalogue
        self.users = users
        self.user_account = []

    def __str__(self):
        return f"Active loans: {len(self.user_account)}"

    def print_available_books(self):
        available = [
            book for book in self.catalogue.book_list
            if book.get_available_copies() > 0
        ]

        if not available:
            print("No books available.")
            return

        for book in available:
            print(book)

    def borrow_book(self, user_name, book_title):
        """Borrow one available copy and record its due date."""
        user = self.users.get_user_details(user_name)

        if user is None:
            raise ValueError("User not found.")

        matching_books = self.catalogue.search_book_title(book_title)
        book = next(
            (
                item for item in matching_books
                if item.get_available_copies() > 0
            ),
            None,
        )

        if book is None:
            raise ValueError("Book not found or no copies are available.")

        # Prevent the same user borrowing the same title twice at once.
        duplicate_loan = any(
            loan["user_name"].casefold() == user.user_name.casefold()
            and loan["book_id"] == book.ID
            for loan in self.user_account
        )
        if duplicate_loan:
            raise ValueError("This user already has this book on loan.")

        checkout_date = datetime.now()
        due_date = checkout_date + timedelta(days=self.LOAN_PERIOD_DAYS)

        loan = {
            "user_name": user.user_name,
            "book_id": book.ID,
            "book_title": book.title,
            "checkout_date": checkout_date,
            "due_date": due_date,
        }

        book.borrowed_copies += 1
        self.catalogue.available_books[book.ID] = book.get_available_copies()
        self.user_account.append(loan)

        return loan

    def return_book(self, user_name, book_title):
        """Return a book currently borrowed by the specified user."""
        user = self.users.get_user_details(user_name)

        if user is None:
            raise ValueError("User not found.")

        for loan in self.user_account:
            if (
                loan["user_name"].casefold() == user.user_name.casefold()
                and loan["book_title"].casefold() == book_title.casefold()
            ):
                book = next(
                    (
                        item for item in self.catalogue.book_list
                        if item.ID == loan["book_id"]
                    ),
                    None,
                )

                if book is None:
                    raise ValueError(
                        "The catalogue entry for this loan no longer exists."
                    )

                book.borrowed_copies -= 1
                self.catalogue.available_books[book.ID] = (
                    book.get_available_copies()
                )
                self.user_account.remove(loan)
                return loan

        raise ValueError("No matching active loan was found.")

    def count_borrowed_books(self, user_name):
        user = self.users.get_user_details(user_name)

        if user is None:
            raise ValueError("User not found.")

        return sum(
            loan["user_name"].casefold() == user.user_name.casefold()
            for loan in self.user_account
        )

    def get_overdued(self, as_of=None):
        """Return active loans whose due date has passed."""
        if as_of is None:
            as_of = datetime.now()

        return [
            loan for loan in self.user_account
            if loan["due_date"] < as_of
        ]
