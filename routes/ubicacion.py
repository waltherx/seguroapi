from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Ubicacion import Ubicacion

# Models
from models.ubicacionModel import UbicacionModel

UbicacionApi = Blueprint("ubicacion_blueprint", __name__)


@UbicacionApi.route("/view/<id>", methods=["GET"])
def view_ubicacion(id: int):
    try:
        if request.method == "GET":
            ubicacion = UbicacionModel.view_ubicacion(id)
            if ubicacion is not None:
                return jsonify(ubicacion), 200
            else:
                return jsonify({"message": "no se encontro ubicacion!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UbicacionApi.route("/last/<ci>", methods=["GET"])
def last_ubicacion(ci:int):
    try:
        if request.method == "GET":
            ubicacion = UbicacionModel.last_ubicacion(ci)
            if ubicacion is not None:
                return jsonify(ubicacion), 200
            else:
                return jsonify({"message": "no se encontro ubicacion!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_ubicacion_data(data, is_update: bool):
    if is_update:
        required_fields = ["id", "nombre"]
    else:
        required_fields = ["persona_ci", "dispositivo_id", "latitud", "longitud"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    id = data.get("id", 0)
    latitud = data["latitud"]
    longitud = data["longitud"]
    hora = data.get("hora", "")
    persona_ci = data["persona_ci"]
    dispositivo_id = data["dispositivo_id"]
    return Ubicacion(id, latitud, longitud, hora, persona_ci, dispositivo_id)


@UbicacionApi.route("/add", methods=["POST"])
def add_ubicacion():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        ubicacion = validate_ubicacion_data(data, False)
        affected_rows = UbicacionModel.add_ubicacion(ubicacion)
        if affected_rows == 1:
            return jsonify({"message": "Ubicacion Agregada!"}), 201
        else:
            return jsonify({"message": "Error al insertar"}), 404
    except BadRequest as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@UbicacionApi.route("/delete", methods=["DELETE"])
def delete_ubicacion(id: int):
    try:
        if request.method == "DELETE":
            affected_rows = UbicacionModel.delete_ubicacion(id)
            if affected_rows == 1:
                return jsonify({"message": "Ubicacion Eliminada!"}), 200
            else:
                return jsonify({"message": "Ubicacion  no Eliminada"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
