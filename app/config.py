import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = "postgresql://miguelmagalhaes:yourpassword@db:5432/miguelmagalhaes"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True 
    # SQLALCHEMY_DATABASE_URI = 'postgresql://miguelmagalhaes:yourpassword@localhost/miguelmagalhaes'
    # SQLALCHEMY_DATABASE_URI = "postgresql://myuser:mypassword@localhost:5432/mydb"

    # SQLALCHEMY_DATABASE_URI = "postgresql://dev:yourpassword@localhost:5432/devdb"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URI', 'postgresql://miguelmagalhaes:yourpassword@http://127.0.0.1:8000:5432/miguelmagalhaes'
    )



class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URI', 'postgresql://username:password@localhost/test_db'
    )
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing

class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI', 'postgresql://username:password@http://127.0.0.1:8000:5432/prod_db'
    )
