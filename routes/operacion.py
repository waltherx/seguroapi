from flask import Blueprint, jsonify, request

# Entities
from models.entities.Operacion import Operacion

# Models
from models.operacionModel import OperacionModel

OperacionApi = Blueprint("operacion_blueprint", __name__)


@OperacionApi.route("/<ci>")
def get_operacion(ci):
    try:
        operacion = OperacionModel.get_operacion(ci)
        if operacion != None:
            return jsonify(operacion), 200
        else:
            return jsonify({"msg": "no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500