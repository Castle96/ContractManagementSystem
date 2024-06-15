from flask import Flask
from .config import Config
from .database import db
from .views import contracts_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(contracts_bp)
    
    with app.app_context():
        db.create_all()
    
    return app
