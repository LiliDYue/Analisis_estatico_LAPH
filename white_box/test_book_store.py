# -*- coding: utf-8 -*-

"""
White-box unit testing of book store.
"""
import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore

class TestBook(unittest.TestCase):
    """
    Unit tests for the Book class.
    """

    def test_display_prints_correct_info(self):
        """Test that display prints all book details correctly."""
        book = Book("1984", "George Orwell", 15.99, 5)
        with patch("builtins.print") as mocked_print:
            book.display()
            mocked_print.assert_any_call("Title: 1984")
            mocked_print.assert_any_call("Author: George Orwell")
            mocked_print.assert_any_call("Price: $15.99")
            mocked_print.assert_any_call("Quantity: 5")


class TestBookStore(unittest.TestCase):
    """
    Unit tests for the BookStore class.
    """

    def setUp(self):
        """Initialize BookStore and sample books."""
        self.store = BookStore()
        self.book1 = Book("1984", "George Orwell", 15.99, 5)
        self.book2 = Book("Brave New World", "Aldous Huxley", 12.5, 3)

    def test_add_book_appends_book(self):
        """Test that add_book adds a book to the store."""
        with patch("builtins.print") as mocked_print:
            self.store.add_book(self.book1)
            self.assertIn(self.book1, self.store.books)
            mocked_print.assert_any_call("Book '1984' added to the store.")

    def test_display_books_empty_store(self):
        """Test display_books prints correct message when store is empty."""
        with patch("builtins.print") as mocked_print:
            self.store.display_books()
            mocked_print.assert_any_call("No books in the store.")

    def test_display_books_with_books(self):
        """Test display_books prints all books correctly."""
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)
        with patch("builtins.print") as mocked_print:
            self.store.display_books()
            mocked_print.assert_any_call("Books available in the store:")
            mocked_print.assert_any_call("Title: 1984")
            mocked_print.assert_any_call("Title: Brave New World")

    def test_search_book_found(self):
        """Test search_book prints correct output when book is found."""
        self.store.add_book(self.book1)
        with patch("builtins.print") as mocked_print:
            self.store.search_book("1984")
            mocked_print.assert_any_call("Found 1 book(s) with title '1984':")
            mocked_print.assert_any_call("Title: 1984")

    def test_search_book_not_found(self):
        """Test search_book prints correct message when no book is found."""
        self.store.add_book(self.book1)
        with patch("builtins.print") as mocked_print:
            self.store.search_book("Unknown Book")
            mocked_print.assert_any_call("No book found with title 'Unknown Book'.")


class TestBookStoreMain(unittest.TestCase):
    """
    Integration tests for the main function of BookStore.
    """

    @patch("builtins.input", side_effect=["4"])
    @patch("builtins.print")
    def test_main_exit(self, mocked_print, mocked_input):
        """Test that main prints exiting message when user chooses 4."""
        from white_box.book_store import main
        
        main()
        mocked_print.assert_any_call("Exiting...")

    @patch("builtins.input", side_effect=["1", "4"])
    @patch("builtins.print")
    def test_main_display_books_empty(self, mocked_print, mocked_input):
        """Test main displays books when store is empty."""
        from white_box.book_store import main
        
        main()
        mocked_print.assert_any_call("No books in the store.")