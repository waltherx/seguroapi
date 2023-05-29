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


@AlergiaApi.route("/view/<id>", methods=["GET"])
def view_alergia(id):
    try:
        alergia = AlergiaModel.view_alergia(id)
        if alergia is not None:
            return jsonify(alergia), 200
        else:
            return jsonify({"message": "no se encontro alergia!"}), 404
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


def validate_alergia_data(data):
    required_fields = ["id_paciente", "nombre"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )

    id_paciente = data["id_paciente"]
    nombre = data["nombre"]
    descripcion = data.get("descripcion", "")
    gravedad = data.get("gravedad", "")
    reaccion = data.get("reaccion", "")

    return Alergia(None, nombre, descripcion, gravedad, reaccion, id_paciente)


@AlergiaApi.route("/add", methods=["POST"])
def add_alergia():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        alergia = validate_alergia_data(data)
        affected_rows = AlergiaModel.add_alergia(alergia)

        if affected_rows == 1:
            return jsonify({"message": "Alergia Agregada!"}), 201
        else:
            return jsonify({"message": "Error al insertar"}), 500

    except BadRequest as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@AlergiaApi.route("/update/<id>", methods=["PUT"])
def update_alergia(id):
    try:
        data = request.json
        id = data["id"]
        nombre = data["nombre"]
        descripcion = data.get("descripcion", "")
        gravedad = data.get("gravedad", "")
        reaccion = data.get("reaccion", "")
        paciente_id = data["paciente_id"]

        alergia = Alergia(id, nombre)
        affected_rows = AlergiaModel.update_alergia(alergia)

        if affected_rows == 1:
            return jsonify(alergia.id)
        else:
            return jsonify({"message": "No alergia updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/delete/<id>", methods=["DELETE"])
def delete_alergia(id):
    try:
        affected_rows = AlergiaModel.delete_alergia(id)
        if affected_rows == 1:
            return jsonify({"message": "Alergia Eliminada!"}), 200
        else:
            return jsonify({"message": "Alergia  no Eliminada"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
