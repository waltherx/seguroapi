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
            return jsonify({"msg": "Operaciones no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

def validate_operacion_data(data):
    pass
    
@OperacionApi.route("/view/<id>", methods=["GET"])
def view_operacion(id):
    try:
        if request.method == "GET":
            ope = OperacionModel.view_operacion(id)
            if ope is not None:
                return jsonify(ope), 200
            else:
                return jsonify({"message": "no se encontro Operacion!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@OperacionApi.route("/update/<id>", methods=["PUT"])
def update_operacion(id):
    try:
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]
        ope = Operacion(id, nombre, direccion, lat, long)
        affected_rows = OperacionModel.update_operacion(ope)
        if affected_rows == 1:
            return jsonify({"message": "Operacion updated"})
        else:
            return jsonify({"message": "No Operacion updated"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@OperacionApi.route("/delete/<id>", methods=["DELETE"])
def delete_operacion(id):
    try:
        if request.method=="DELETE":
            affected_rows = OperacionModel.delete_operacion(id)
            if affected_rows == 1:
                return jsonify({"message": "Operacion Eliminado!"}), 404
            else:
                return jsonify({"message": "Operacion no Eliminado!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
