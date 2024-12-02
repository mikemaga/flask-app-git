from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import Config
from flask_migrate import Migrate

# app = Flask(__name__)
# Define SQLAlchemy instance globally
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='app.config.DevelopmentConfig'):
    """Application factory."""
    app = Flask(__name__)
 
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    

    # Initialize the database and tables
    # with app.app_context():
    #     db.create_all()

    # Register Blueprints (modular routes)
    from app.routes.general import general_bp
    from app.routes.standings import standings_bp
    from app.routes.competitions import competitions_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(standings_bp)
    app.register_blueprint(competitions_bp)
    # Initialize the database and tables
    with app.app_context():
        db.create_all()
    # Schedule background tasks (optional)
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(lambda: fetch_standings(), 'interval', days=1)
    # scheduler.start()

    return app
