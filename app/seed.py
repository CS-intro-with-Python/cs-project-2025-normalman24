# app/seed.py
from .models import db, Book, Impression
def seed_database():
    """Add initial books and impressions if database is empty."""
    if Book.query.first() is None:
        print("Seeding database with sample books...")

        books_data = [
            {
                "title": "Dune",
                "author": "Frank Herbert",
                "description": "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world.",
                "year": 1965,
                "pages": 688,
                "pages": 688,
                "cover_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Dune-FrankHerbert-1965-bookjacket.jpg/220px-Dune-FrankHerbert-1965-bookjacket.jpg"
            },
            {
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "description": "Bilbo Baggins is a hobbit who enjoys a comfortable life until a wizard named Gandalf recruits him for an adventure.",
                "year": 1937,
                "pages": 310,
                "cover_url": "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_cover.jpg"
            },
            {
                "title": "Atomic Habits",
                "author": "James Clear",
                "description": "An easy & proven way to build good habits & break bad ones through tiny changes.",
                "year": 2018,
                "pages": 320,
                "cover_url": "https://upload.wikimedia.org/wikipedia/en/9/93/Atomic_Habits.jpg"
            }
        ]

        impressions_data = [
            {"review": "A masterpiece...", "score": 10, "reading_time": "3 weeks"},
            {"review": "Charming, adventurous...", "score": 9, "reading_time": "10 days"},
            {"review": "Practical, science-backed...", "score": 8, "reading_time": "less than 1 hour"}
        ]

        for book_data, imp in zip(books_data, impressions_data):
            book = Book(**book_data)
            db.session.add(book)
            db.session.flush()  # Get book.id

            impression = Impression(
                book_id=book.id,
                review=imp["review"],
                score=imp["score"],
                reading_time=imp["reading_time"]
            )
            db.session.add(impression)

        db.session.commit()
        print("Database seeded successfully!")
    else:
        print("Database already has data. Skipping seed.")