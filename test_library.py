
import unittest
from datetime import datetime, timedelta

from catalogue_app import Book, Book_list, User, User_list, Loans


class TestBookCatalogue(unittest.TestCase):
    def setUp(self):
        self.catalogue = Book_list()
        self.book = Book(
            None, "Example Book", "Example Author",
            "Example Press", "2024", 2, "2024"
        )

    def test_book_starts_with_expected_copies(self):
        self.assertEqual(self.book.get_total_copies(), 2)
        self.assertEqual(self.book.get_available_copies(), 2)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            Book(None, "", "Example Author", "Press", "2024", 1, "2024")

    def test_add_book_and_search_case_insensitively(self):
        self.catalogue.add_book(self.book)
        result = self.catalogue.search_book_title("example book")
        self.assertEqual(result, [self.book])

    def test_duplicate_title_and_author_is_rejected(self):
        self.catalogue.add_book(self.book)
        duplicate = Book(
            None, "EXAMPLE BOOK", "example author",
            "Other Press", "2025", 1, "2024"
        )
        with self.assertRaises(ValueError):
            self.catalogue.add_book(duplicate)

    def test_increase_copies(self):
        self.catalogue.add_book(self.book)
        self.catalogue.increase_copies("Example Book", "Example Author", 3)
        self.assertEqual(self.book.get_total_copies(), 5)
        self.assertEqual(self.catalogue.get_total_copies(), 5)

    def test_separate_catalogues_do_not_share_books(self):
        another_catalogue = Book_list()
        self.catalogue.add_book(self.book)
        self.assertEqual(len(another_catalogue.book_list), 0)


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.users = User_list()
        self.user = User("reader01", "Jamie", "Taylor")
        self.users.add_user(self.user)

    def test_count_users(self):
        self.assertEqual(self.users.count_users(), 1)

    def test_username_lookup_is_case_insensitive(self):
        self.assertIs(
            self.users.get_user_details("READER01"), self.user
        )

    def test_duplicate_username_is_rejected(self):
        duplicate = User("READER01", "Morgan", "Lee")
        with self.assertRaises(ValueError):
            self.users.add_user(duplicate)

    def test_setter_updates_email(self):
        self.user.set_email("jamie@example.test")
        self.assertEqual(self.user.get_email(), "jamie@example.test")

    def test_remove_user(self):
        self.users.remove_user("reader01")
        self.assertEqual(self.users.count_users(), 0)

    def test_missing_user_cannot_be_removed(self):
        with self.assertRaises(ValueError):
            self.users.remove_user("missing")


class TestLoans(unittest.TestCase):
    def setUp(self):
        self.catalogue = Book_list()
        self.users = User_list()
        self.book = Book(
            None, "Example Book", "Example Author",
            "Example Press", "2024", 1, "2024"
        )
        self.catalogue.add_book(self.book)
        self.users.add_user(User("reader01", "Jamie", "Taylor"))
        self.users.add_user(User("reader02", "Morgan", "Lee"))
        self.loans = Loans(self.catalogue, self.users)

    def test_borrow_reduces_available_copies(self):
        self.loans.borrow_book("reader01", "Example Book")
        self.assertEqual(self.book.get_available_copies(), 0)
        self.assertEqual(self.loans.count_borrowed_books("reader01"), 1)

    def test_return_restores_available_copies(self):
        self.loans.borrow_book("reader01", "Example Book")
        self.loans.return_book("reader01", "Example Book")
        self.assertEqual(self.book.get_available_copies(), 1)
        self.assertEqual(self.loans.count_borrowed_books("reader01"), 0)

    def test_unavailable_book_cannot_be_borrowed(self):
        self.loans.borrow_book("reader01", "Example Book")
        with self.assertRaises(ValueError):
            self.loans.borrow_book("reader02", "Example Book")
        self.assertEqual(self.book.get_available_copies(), 0)

    def test_user_cannot_return_another_users_loan(self):
        self.loans.borrow_book("reader01", "Example Book")
        with self.assertRaises(ValueError):
            self.loans.return_book("reader02", "Example Book")
        self.assertEqual(self.book.get_available_copies(), 0)

    def test_unknown_user_cannot_borrow(self):
        with self.assertRaises(ValueError):
            self.loans.borrow_book("missing", "Example Book")

    def test_due_date_is_thirty_days_after_checkout(self):
        loan = self.loans.borrow_book("reader01", "Example Book")
        expected_due_date = loan["checkout_date"] + timedelta(days=30)
        self.assertEqual(loan["due_date"], expected_due_date)

    def test_overdue_loan_is_detected(self):
        loan = self.loans.borrow_book("reader01", "Example Book")
        future = loan["due_date"] + timedelta(days=1)
        overdue = self.loans.get_overdued(as_of=future)
        self.assertEqual(len(overdue), 1)
        self.assertEqual(overdue[0]["user_name"], "reader01")


if __name__ == "__main__":
    unittest.main()
