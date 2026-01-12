import unittest
import tempfile
import os
from app import create_app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app, self.db = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.db_path}'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_add_book(self):
        resp = self.client.post('/api/books', json={
            'title': 'CI Test',
            'author': 'Bot',
            'year': 2026,
            'pages': 1
        })
        self.assertEqual(resp.status_code, 201)

    def test_get_books_empty(self):
        resp = self.client.get('/api/books')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, [])