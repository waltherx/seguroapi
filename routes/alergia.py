from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Alergia import Alergia

# Models
from models.alergiaModel import AlergiaModel

AlergiaApi = Blueprint("alergia_blueprint", __name__)


@AlergiaApi.route("/")
def get_alergias():
    try:
        alergias = AlergiaModel.get_alergias()
        return jsonify(alergias)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/<ci>")
def get_alergia(ci):
    try:
        alergia = AlergiaModel.get_alergia(ci)
        if alergia != None:
            return jsonify(alergia)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_alergia_data(data, is_update: bool):
    if is_update:
        required_fields = ["id", "nombre"]
    else:
        required_fields = ["id_paciente", "nombre"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    id = data.get("id", 0)
    id_paciente = data.get("id_paciente",0)
    nombre = data["nombre"]
    descripcion = data.get("descripcion", "")
    gravedad = data.get("gravedad", "")
    reaccion = data.get("reaccion", "")

    return Alergia(id, nombre, descripcion, gravedad, reaccion, id_paciente)


@AlergiaApi.route("/add", methods=["POST"])
def add_alergia():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        alergia = validate_alergia_data(data, False)
        affected_rows = AlergiaModel.add_alergia(alergia)

        if affected_rows == 1:
            return jsonify({"message": "Alergia Agregada!"}), 200
        else:
            return jsonify({"message": "Error al insertar"}), 404

    except BadRequest as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@AlergiaApi.route("/view/<id>", methods=["GET"])
def view_alergia(id):
    try:
        if request.method == "GET":
            alergia = AlergiaModel.view_alergia(id)
            if alergia is not None:
                return jsonify(alergia), 200
            else:
                return jsonify({"message": "no se encontro alergia!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/update", methods=["PUT", "PATCH"])
def update_alergia():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.get_json()
            alergia = validate_alergia_data(data, True)
            affected_rows = AlergiaModel.update_alergia(alergia)
            if affected_rows == 1:
                return jsonify({"message": "Alergia Actualizada!"}), 200
            else:
                return jsonify({"message": "Alergia no Actualizada!"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/delete/<id>", methods=["DELETE"])
def delete_alergia(id: int):
    try:
        affected_rows = AlergiaModel.delete_alergia(id)
        if affected_rows == 1:
            return jsonify({"message": "Alergia Eliminada!"}), 200
        else:
            return jsonify({"message": "Alergia  no Eliminada"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
