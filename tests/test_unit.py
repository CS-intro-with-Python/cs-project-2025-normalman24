import unittest
from app.models import Book

class TestBookModel(unittest.TestCase):
    def test_book_creation(self):
        book = Book(title="Test", author="Me", year=2025, pages=100)
        self.assertEqual(book.title, "Test")
        self.assertEqual(book.pages, 100)

    def test_score_validation_logic(self):
        valid_scores = [1, 5, 10]
        invalid_scores = [0, 11, -1]
        for s in valid_scores:
            self.assertTrue(1 <= s <= 10)
        for s in invalid_scores:
            self.assertFalse(1 <= s <= 10)