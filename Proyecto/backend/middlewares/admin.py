from flask import request, jsonify, g

# Token de prueba (en producción, usa JWT)
ADMIN_TOKEN = 'UnTokenSeguro'

# Middleware para verificar el token de administrador
def admin_required(f):
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {ADMIN_TOKEN}":
            return jsonify({"error": "Acceso no autorizado"}), 403
        return f(*args, **kwargs)
    return decorated_function