from sqlalchemy import text
from app import db

def get_tables():
    result = db.session.execute(
        text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    )
    return [row[0] for row in result.fetchall()]
