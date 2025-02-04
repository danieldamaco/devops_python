from flask import Blueprint, jsonify, g

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=['GET'])
def hola():
    return g.algo