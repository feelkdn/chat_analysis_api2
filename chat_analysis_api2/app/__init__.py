# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # CORS 설정: 모든 origin 허용 + credentials 지원
    CORS(app, supports_credentials=True)

    # 블루프린트 등록
    from app.routes.routes import analysis_bp
    app.register_blueprint(analysis_bp)

    return app
