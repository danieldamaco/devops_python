from flask import Flask
from backend.routes import register_routes
from backend.middlewares.redis import redis_client

def create_app():
    app = Flask(__name__)
    redis_client()
    register_routes(app)
    return app