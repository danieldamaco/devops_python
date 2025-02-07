from flask import Blueprint, jsonify, request
from backend.middlewares.redis import redis_client
from backend.middlewares.admin import admin_required
import uuid

redis_client = redis_client()

order_bp = Blueprint("orders", __name__)

@order_bp.route("/orders", methods=['POST'])
def create_orders():
    """
    Crea la orden recibiendo el nombre del cliente por el cuerpo de la peticio. La informacion es almacenada 
    en la base de datos redis. 
    Responde la informacion de la peticion: status y id de la orden. 
    """
    try:
        body = request.get_json()
        name = body.get("name")
        pizza = body.get("pizza-type")
    except Exception as err:
        print(err)
        return jsonify({"error": f"{err}"})

    try:
        id = uuid.uuid4()
        redis_client.hset(str(id), mapping={"name": str(name), "status":'created', "pizza":str(pizza)})
        return jsonify({"order":{"status": f'created', "id": f'{id}'}}), 200
    except Exception as err:
        print(err)
        return jsonify({"error": f"{err}"})
    


@order_bp.route("/orders/<uuid:order_id>", methods=['GET'])
def get_orders(order_id):
    """
    Verifica si la orden se encuentra dentro de la estructura de datos, en dado caso
    devuelve el status de la orden. Si no existe, devuelve que no existe dicha orden. 
    """
    try:
        order = redis_client.hgetall(str(order_id))
        if not order: raise Exception("Id no valido")
        return jsonify({"order_id": f'{order_id}', "status":f'{order['status']}' })
    except Exception as err:
        return jsonify({"error": f"{err}"})

@order_bp.route("/orders/<uuid:order_id>", methods=['DELETE'])
@admin_required
def delete_orders(order_id):
    """
    Elimina la orden con el id pasado por los path parameters. Si no existe arroja el error Id no valido. 
    """

    try:
        order = redis_client.hdel(str(order_id), "name", "status", "pizza")
        if not order: raise Exception("Id no valido")
        return jsonify({"order_id": f'{order_id}', "status":"deleted" })
    except Exception as err:
        return jsonify({"error": f"{err}"})