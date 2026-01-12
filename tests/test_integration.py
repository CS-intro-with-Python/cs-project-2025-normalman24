import unittest
from app import create_app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app, self.db = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()

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