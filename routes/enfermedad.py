from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Enfermedad import Enfermedad

# Models
from models.enfermedadModel import EnfermedadModel

EnfermedadApi = Blueprint("enfermedad_blueprint", __name__)


@EnfermedadApi.route("/")
def get_enfermedads():
    try:
        enfermedads = EnfermedadModel.get_enfermedads()
        return jsonify(enfermedads)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/<ci>")
def get_enfermedad(ci):
    try:
        enfermedad = EnfermedadModel.get_enfermedad(ci)
        if enfermedad != None:
            return jsonify(enfermedad)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/view/<id>", methods=["GET"])
def view_enfermedad(id):
    try:
        if request.method == "GET":
            enfermedad = EnfermedadModel.view_enfermedad(id)
            if enfermedad != None:
                return jsonify(enfermedad)
            else:
                return jsonify({"message": "no se encontro enfermedad"}), 404
        else:
            return jsonify({"message": "methodo http no valido"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_data(data, op):
    if op:
        required_fields = ["id", "nombre", "paciente_id"]
    else:
        required_fields = ["nombre", "paciente_id"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    id = data.get("id", 0)
    nombre = data["nombre"]
    descripcion = data.get("descripcion", "")
    causa = data.get("causa", "")
    sintoma = data.get("sintoma", "")
    diagnostico = data.get("diagnostico", "")
    paciente_id = data["paciente_id"]

    return Enfermedad(id, nombre, descripcion, causa, sintoma, diagnostico, paciente_id)


@EnfermedadApi.route("/add", methods=["POST"])
def add_enfermedad():
    try:
        if request.method == "POST":
            data = request.json
            enfermedad = validate_data(data, False)
            affected_rows = EnfermedadModel.add_enfermedad(enfermedad)
            if affected_rows == 1:
                return jsonify({"message": "Enfermedad insertada correctamente"})
            else:
                return jsonify({"message": "Error al insertar la enfermedad"}), 500
        else:
            return jsonify({"message": "Método no permitido"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/update", methods=["PUT", "PACTH"])
def update_enfermedad():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.json
            enfermedad = validate_data(data, True)
            print(enfermedad.to_JSON())
            affected_rows = EnfermedadModel.update_enfermedad(enfermedad)
            if affected_rows == 1:
                return jsonify({"message": "Enfermedad Actualizada correctamente"})
            else:
                return jsonify({"message": "Error al Actualizar la enfermedad"}), 500
        else:
            return jsonify({"message": "Método no permitido"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/delete/<id>", methods=["DELETE"])
def delete_enfermedad(id):
    try:
        affected_rows = EnfermedadModel.delete_enfermedad(id)
        if affected_rows == 1:
            return jsonify({"message": "enfermedad deleted"})
        else:
            return jsonify({"message": "No enfermedad deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
