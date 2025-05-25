# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # �������Ʈ ���
    from app.routes.routes import analysis_bp
    app.register_blueprint(analysis_bp)

    return app
