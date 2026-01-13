import unittest
import requests
from app.models import Book

class TestBookModel(unittest.TestCase):
    def test_book_creation(self):
        book = Book(title="Test", author="Me", year=2025, pages=100)
        self.assertEqual(book.title, "Test")
        self.assertEqual(book.pages, 100)

class TestServerErrorHandling(unittest.TestCase):
    def test_invalid_book_submission_returns_400(self):
        try:
            response = requests.post(
                "http://localhost:5000/api/books",
                json={"title": "Only title"}
            )
            self.assertEqual(response.status_code, 400)
        except requests.ConnectionError:
            self.fail("Server not running. Start with: docker compose up -d")