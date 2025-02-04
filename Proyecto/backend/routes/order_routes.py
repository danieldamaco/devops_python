from flask import Blueprint, jsonify, g, request
from backend.data_structures.hola import Pizzas, Orders, Users, Admin
import uuid

order_bp = Blueprint("orders", __name__)

@order_bp.route("/orders/", methods=['POST'])
def create_orders():
    """
    Crea la orden recibiendo el nombre del cliente por el cuerpo de la peticio. La informacion es almacenada 
    en la variable global g.order. 
    Responde la informacion de la peticion: status y id de la orden. 
    """
    body = request.get_json()
    name = body.get("name")

    if not name: return {"error": "Se requiere name en body. "}

    id = uuid.uuid4()
    user= Users(name=name)
    order= Orders(id=id, status='created', user=user, pizza='')
    g.order.append(order)

    return jsonify({"order":{"status": f'{order.status}', "id": f'{order.id}'}})

@order_bp.route("/orders/<int:order_id>", methods=['GET'])
def get_orders(order_id):
    """
    Verifica si la orden se encuentra dentro de la estructura de datos, en dado caso
    devuelve el status de la orden. Si no existe, devuelve que no existe dicha orden. 
    """
    for order in g.order:
        if order.id == order_id:
            return jsonify({"order_id": f'{order_id}', "status":f'{order.status}' })
        else:
            continue
    
    return jsonify({"error": "orden no encontrada"})

@order_bp.route("/orders/<int:order_id>", methods=['DELETE'])
def delete_orders(order_id):
    """
    Elimina la orden con el id pasado por los path parameters. Si no existe 
    """
    for order in g.order:
        if order.id == order_id:
            order.status = "deleted"
            return jsonify({"order":{"status": "deleted", "id": f'{order_id}'}})
        else:
            continue
    
    return jsonify({"error": "orden no encontrada"})