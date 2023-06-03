from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

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


def validate_operacion_data(data, is_update):
    if is_update:
        required_fields = ["id", "tipo", "fecha"]
    else:
        required_fields = ["id_paciente", "tipo", "fecha"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    id = data.get("id", 0)
    id_paciente = data.get("id_paciente", 0)
    tipo = data["tipo"]
    fecha = data["fecha"]
    descripcion = data.get("descripcion", "")
    return Operacion(id, tipo, fecha, descripcion, id_paciente)


@OperacionApi.route("/add", methods=["POST"])
def add_operacion():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        op = validate_operacion_data(data, False)
        affected_rows = OperacionModel.add_operacion(op)

        if affected_rows == 1:
            return jsonify({"message": "Vacuna Agregada!"}), 201
        else:
            return jsonify({"message": "Error al insertar"}), 500

    except BadRequest as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


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


@OperacionApi.route("/update", methods=["PUT"])
def update_operacion():
    try:
        data = request.get_json()
        ope = validate_operacion_data(data, True)
        print(ope.to_JSON())
        affected_rows = OperacionModel.update_operacion(ope)
        if affected_rows == 1:
            return jsonify({"message": "Operacion Actualizada!"}), 200
        else:
            return jsonify({"message": "Operacion no Actualizada!"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@OperacionApi.route("/delete/<id>", methods=["DELETE"])
def delete_operacion(id: int):
    try:
        if request.method == "DELETE":
            affected_rows = OperacionModel.delete_operacion(id)
            if affected_rows == 1:
                return jsonify({"message": "Operacion Eliminado!"}), 200
            else:
                return jsonify({"message": "Operacion no Eliminado!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
