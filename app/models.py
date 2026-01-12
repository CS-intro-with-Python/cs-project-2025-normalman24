from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    cover_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "year": self.year,
            "pages": self.pages
        }

class Impression(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    review = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    reading_time = db.Column(db.String(50), nullable=False)