from flask import Blueprint, jsonify, g,request
from backend.middlewares.admin import admin_required

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu", methods=['GET'])
def get_menu():
    return jsonify({"types": f'{g.pizzas.types}'})

@admin_required
@menu_bp.route("/menu", methods=["POST"])
def change_menu():
    body = request.get_json()
    new_pizza = body.get("new_pizza")

    if not new_pizza: return jsonify({"error": "No hay nuevo tipo de pizza en body."})

    g.pizzas.types.append(new_pizza)

    return jsonify({"success": "Nueva pizza agregada con éxito"})

@admin_required #NEcesito eliminar una pizza
@menu_bp.route("/menu", methods=["DELETE"])
def change_menu():
    body = request.get_json()
    delete_pizza = body.get("delete_pizza")

    if not delete_pizza: return jsonify({"error": "No hay nuevo tipo de pizza en body."})

    g.pizzas.types.append(delete_pizza)

    return jsonify({"success": "Nueva pizza agregada con éxito"})