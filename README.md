# BookHub

[Link](https://cs-project-2025-normalman24.onrender.com/)

## Description
BookHub is a web platform that allows users to share the books they have read.  
When someone finishes a book, they can upload it to the platform, including:
- Book cover (URL)
- Author
- Description
- Year of publication
- Number of pages

Users can also add their **impressions**, which include:
- Text review
- Overall score (1–10)
- Reading period (e.g., "3 days", "less than 1 hour")

## Setup
Use Docker Compose (required by project criteria):

```bash
docker compose up --build
```

The application will be available at:  
- Web interface: http://localhost:5000  
- All books (with IDs): http://localhost:5000/books  
- API documentation: http://localhost:5000/docs

## Requirements
- Docker and Docker Compose
- Python 3.11
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1
- flask-swagger-ui 0.0.3
- requests 2.32.5

## Git
Stable version is maintained on the `main` branch:

```bash
git checkout main
```

## How to Run Tests
From the project root:

```bash
pip install -r requirements.txt
python tests/test_integration.py # integration tests
python -m unittest tests/test_unit.py -v # unit tests
```

## How to Get Logs
When running with Docker Compose:

```bash
docker compose logs -f web
```

Logs include:
- Application startup
- Book additions
- Impression submissions
- Errors (invalid input, server issues)

## Technologies Used
- **Backend**: Flask
- **Database**: SQLite via `Flask-SQLAlchemy`
- **Client**: Browser-based HTML interface
- **API Docs**: Swagger UI (`/docs`)
- **Containerization**: Docker Compose
- **CI/CD**: GitHub Actions + Render.com
- **Testing**: `unittest` for unit testing + `requests` for integration testing