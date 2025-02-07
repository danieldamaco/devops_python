from flask import Blueprint, jsonify, request
from backend.middlewares.admin import admin_required
from backend.middlewares.redis import redis_client
import json

redis_client = redis_client()

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu", methods=['GET'])
def get_menu():
    try:
        menu = redis_client.hgetall("menu")
        return jsonify({"menu": f'{menu}'}), 200
    except Exception as err:
        return jsonify({"error": f"{err}"})

@menu_bp.route("/menu", methods=["POST", "DELETE"])
@admin_required
def change_menu():
    """
    Modifica el menu del restaurante. Si el metod es POST agrega una pizza, si es DELETE la elimina. 
    """
    if request.method == 'POST':
        body = request.get_json()
        new_pizza = body.get("new_pizza")
        try:
            #Busqueda y cambio de formato de la entrada menu de la base de datos. 
            pizza_types = redis_client.hgetall(str("menu"))
            pizza_types = pizza_types["types"]
            pizza_types = pizza_types.replace("'", '"') 
            pizza_types = json.loads(pizza_types)

            pizza_types.append(new_pizza)
            redis_client.hset("menu", mapping={"types": str(pizza_types)})
            return jsonify({"success": "Nueva pizza agregada con éxito"}), 201
        except Exception as err:
            return jsonify({"error": f'{err}'}), 400
    elif request.method == 'DELETE':
        print(request.method)
        body = request.get_json()
        delete_pizza = body.get("delete_pizza")
        try:
            #Busqueda y cambio de formato de la entrada menu de la base de datos. 
            pizza_types = redis_client.hgetall(str("menu"))
            pizza_types = pizza_types["types"]
            pizza_types = pizza_types.replace("'", '"') 
            pizza_types = json.loads(pizza_types)


            pizza_types.remove(delete_pizza)
            redis_client.hset("menu", mapping={"types": str(pizza_types)})
            return jsonify({"success": "Pizza eliminada con éxito"}), 200
        except Exception as err:
            return jsonify({"error": f'{err}'}), 400