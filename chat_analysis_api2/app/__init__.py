# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # 블루프린트 등록
    from app.routes.routes import analysis_bp
    app.register_blueprint(analysis_bp)

    return app
