from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Dispositivo import Dispositivo

# Models
from models.dispositivoModel import DispositivoModel

DispositivoApi = Blueprint("dispositivo_blueprint", __name__)

@DispositivoApi.route("/view/<id>", methods=["GET"])
def view_dispositivo(id: int):
    try:
        if request.method == "GET":
            dispositivo = DispositivoModel.view_dispositivo(id)
            if dispositivo is not None:
                return jsonify(dispositivo), 200
            else:
                return jsonify({"message": "no se encontro dispositivo!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_dispositivo_data(data, is_update: bool):
    if is_update:
        required_fields = ["id", "nombre"]
    else:
        required_fields = ["nombre"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    id = data.get("id", 0)
    nombre = data["nombre"]    
    return Dispositivo(id, nombre)


@DispositivoApi.route("/add", methods=["POST"])
def add_dispositivo():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        dispositivo = validate_dispositivo_data(data, False)
        print(dispositivo.to_JSON())
        affected_rows = DispositivoModel.add_dispositivo(dispositivo)
        if affected_rows == 1:
            return jsonify({"message": "Dispositivo Agregado!"}), 201
        else:
            return jsonify({"message": "Error al insertar"}), 500
    except BadRequest as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@DispositivoApi.route("/delete", methods=["DELETE"])
def delete_dispositivo(id: int):
    try:
        if request.method == "DELETE":
            affected_rows = DispositivoModel.delete_dispositivo(id)
            if affected_rows == 1:
                return jsonify({"message": "Dispositivo Eliminado!"}), 200
            else:
                return jsonify({"message": "Dispositivo  no Eliminado"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
