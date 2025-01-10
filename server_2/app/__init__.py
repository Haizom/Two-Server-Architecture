from flask import Flask
from .routes import web_bp

def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.secret_key = 'supersecretkey'  # Required for flashing messages
    app.register_blueprint(web_bp)
    return app
