# from flask import Flask, request, jsonify

# # Token de prueba (en producción, usa JWT)
# ADMIN_TOKEN = "UnTokenSecreto"

# # Middleware para verificar el token de administrador
# def admin_required(f):
#     def decorated_function(*args, **kwargs):
#         token = request.headers.get("Authorization")
#         if not token or token != f"Bearer {ADMIN_TOKEN}":
#             return jsonify({"error": "Acceso no autorizado"}), 403
#         return f(*args, **kwargs)
#     return decorated_function

# @app.route("/")
# def hello():
#     return "Bienvenido a pizzas (agregue nombre atractivo jeje)"

# @app.route("/menu")
# def menu():
#     return "Aquí aparecerá el menú"

# @app.route("/order", methods=["POST"])
# def order():
#     return "Aquí crearé un id unico para que lo devuelva."

# @app.route("/order/<str:order_id>", methods=["GET"])
# def order():
#     return "Aquí Aparecerá el status del pedido."

# @app.route("/order/<str:order_id>", methods=["DELETE"])
# def order():
#     return "Aquí se borrará a orden."

# #Agregar pizza al menu (admin) POST -> /menu como admin. 
# #Eliminar pizza al menu (admin) DELETE -> /menu como admin. 
# #Cancelar orden sin importar el status DELETE -> order como admin. 




# # Ruta con múltiples métodos HTTP
# @app.route("/admin", methods=["GET", "POST", "PUT", "DELETE"])
# @admin_required  # Se ejecuta antes de la función
# def admin():
#     if request.method == "GET":
#         return jsonify({"message": "GET: Datos de admin"})
#     elif request.method == "POST":
#         #Agregar pizza al menu 
#         return jsonify({"message": "POST: Creado con éxito"})
#     elif request.method == "PUT":
#         return jsonify({"message": "PUT: Actualizado con éxito"})
#     elif request.method == "DELETE":
#         return jsonify({"message": "DELETE: Eliminado con éxito"})

from backend.routes.user_routes import user_bp
from backend.routes.menu_routes import menu_bp
from backend.routes.order_routes import order_bp


def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(menu_bp, url_prefix="/api")
    app.register_blueprint(order_bp, url_prefix="/api")
