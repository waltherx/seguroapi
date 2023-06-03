from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Vacuna import Vacuna

# Models
from models.vacunaModel import VacunaModel

VacunaApi = Blueprint("vacuna_blueprint", __name__)


@VacunaApi.route("/<ci>")
def get_vacuna(ci):
    try:
        vacuna = VacunaModel.get_vacuna(ci)
        if vacuna != None:
            return jsonify(vacuna), 200
        else:
            return jsonify({"msg": "no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@VacunaApi.route("/view/<id>", methods=["GET"])
def view_vacuna(id):
    try:
        if request.method == "GET":
            alergia = VacunaModel.view_vacuna(id)
            if alergia is not None:
                return jsonify(alergia), 200
            else:
                return jsonify({"message": "no se encontro alergia!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_vacuna_data(data, is_update: bool):
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
    id_paciente = data.get("id_paciente", 0)
    nombre = data["nombre"]
    dosis = data.get("dosis", 0)
    return Vacuna(id, nombre, dosis, id_paciente)

@VacunaApi.route("/add", methods=["POST"])
def add_vacuna():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        vacuna = validate_vacuna_data(data, False)
        print(vacuna.to_JSON())
        affected_rows = VacunaModel.add_vacuna(vacuna)

        if affected_rows == 1:
            return jsonify({"message": "Vacuna Agregada!"}), 201
        else:
            return jsonify({"message": "Error al insertar"}), 500

    except BadRequest as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@VacunaApi.route("/update", methods=["PUT", "PATCH"])
def update_vacuna():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.json
            ambu = validate_vacuna_data(data, True)
            if VacunaModel.update_vacuna(ambu):
                return jsonify({"message": "Vacuna Actualizada!"}), 200
            else:
                return jsonify({"message": "Vacuna no Actualizada!"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@VacunaApi.route("/delete", methods=["DELETE"])
def delete_vacuna(id):
    try:
        if request.method == "DELETE":
            affected_rows = VacunaModel.delete_vacuna(id)
            if affected_rows == 1:
                return jsonify({"message": "Vacuna Eliminada!"}), 200
            else:
                return jsonify({"message": "Vacuna  no Eliminada"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
