import sys
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent))

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all() 

if __name__ == '__main__':
    app.run(debug=True)  # Use `debug=True` for development mode