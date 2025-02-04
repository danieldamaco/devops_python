from flask import Flask, g
from backend.routes import register_routes
from backend.data_structures.hola import Pizzas, Orders, Users, Admin


def create_app():
    app = Flask(__name__)

    @app.before_request
    def inicializar():
        g.order = []
        g.user = {}
        g.admin = Admin(id='1234abcd', token='UnTokenSeguro')
        g.pizzas = Pizzas()

    register_routes(app)
    return app