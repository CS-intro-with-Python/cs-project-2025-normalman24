from app import create_app
from app.seed import seed_database

app, db = create_app()

with app.app_context():
    db.create_all()
    seed_database()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)