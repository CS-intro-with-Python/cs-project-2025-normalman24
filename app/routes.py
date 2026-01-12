from flask import Blueprint, request, jsonify, render_template, current_app, redirect
from .models import db, Book, Impression

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_book', methods=['POST'])
def add_book_form():
    try:
        book = Book(
            title=request.form['title'],
            author=request.form['author'],
            description=request.form.get('description', ''),
            year=int(request.form['year']),
            pages=int(request.form['pages']),
            cover_url=request.form.get('cover_url', '')
        )
        db.session.add(book)
        db.session.commit()
        current_app.logger.info(f"📘 Book added via form: '{book.title}' (ID: {book.id})")
        return redirect('/books')
    except Exception as e:
        current_app.logger.error(f"💥 Error adding book via form: {e}")
        return "Bad Request", 400


@main.route('/add_impression', methods=['POST'])
def add_impression_form():
    try:
        book_id_str = request.form.get('book_id', '').strip()

        # Check if book_id is a positive integer
        if not book_id_str.isdigit():
            return render_template('error.html',
                                   message="Invalid Book ID: Please enter a positive number (e.g., 1, 2, 3).")

        book_id = int(book_id_str)
        if book_id <= 0:
            return render_template('error.html',
                                   message="Invalid Book ID: ID must be greater than 0.")

        # Check if book exists
        book = Book.query.get(book_id)
        if not book:
            return render_template('error.html',
                                   message=f"There is no book with ID {book_id}. Please check that you entered the correct ID.")

        # Validate other fields
        review = request.form.get('review', '').strip()
        score_str = request.form.get('score', '').strip()
        reading_time = request.form.get('reading_time', '').strip()

        if not review or not reading_time:
            return render_template('error.html',
                                   message="Review and reading time are required.")

        if not score_str.isdigit() or not (1 <= int(score_str) <= 10):
            return render_template('error.html',
                                   message="Score must be an integer between 1 and 10.")

        # Save impression
        impression = Impression(
            book_id=book.id,
            review=review,
            score=int(score_str),
            reading_time=reading_time
        )
        db.session.add(impression)
        db.session.commit()
        current_app.logger.info(f"📝 Impression added for book ID {book_id}")
        return redirect('/books')

    except Exception as e:
        current_app.logger.error(f"💥 Unexpected error in add_impression: {e}")
        return render_template('error.html',
                               message="An unexpected error occurred. Please try again."), 500

@main.route('/api/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

@main.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    if not data or not all(k in data for k in ('title', 'author', 'year', 'pages')):
        current_app.logger.warning("❌ Invalid book  missing fields")
        return jsonify({"error": "Missing fields"}), 400

    try:
        book = Book(
            title=data['title'],
            author=data['author'],
            description=data.get('description', ''),
            year=int(data['year']),
            pages=int(data['pages'])
        )
        db.session.add(book)
        db.session.commit()
        current_app.logger.info(f"📘 Book added: '{book.title}' (ID: {book.id})")
        return jsonify(book.to_dict()), 201
    except Exception as e:
        current_app.logger.error(f"💥 Error adding book: {e}")
        return jsonify({"error": "Invalid data"}), 400

@main.route('/api/books/<int:book_id>/impression', methods=['POST'])
def add_impression(book_id):
    book = Book.query.get(book_id)
    if not book:
        current_app.logger.warning(f"⚠️ Book {book_id} not found")
        return jsonify({"error": "Book not found"}), 404

    data = request.json
    required = ['review', 'score', 'reading_time']
    if not data or not all(k in data for k in required):
        current_app.logger.warning("❌ Impression missing fields")
        return jsonify({"error": "Missing impression fields"}), 400

    score = data['score']
    if not isinstance(score, int) or not (1 <= score <= 10):
        current_app.logger.warning(f"⚠️ Invalid score: {score}")
        return jsonify({"error": "Score must be integer 1–10"}), 400

    impression = Impression(
        book_id=book.id,
        review=data['review'],
        score=score,
        reading_time=data['reading_time']
    )
    db.session.add(impression)
    db.session.commit()
    current_app.logger.info(f"📝 Impression added for book {book_id}")
    return jsonify({"message": "Impression added"}), 201

@main.route('/books')
def list_books():
    books = Book.query.all()
    # Preload impressions for each book
    for book in books:
        book.impressions = Impression.query.filter_by(book_id=book.id).all()
    return render_template('books.html', books=books)