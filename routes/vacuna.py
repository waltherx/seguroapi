from flask import Blueprint, jsonify, request

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


@VacunaApi.route("/add", methods=["POST"])
def add_vacuna():
    pass


def validate_vacuna_data(data):
    pass


@VacunaApi.route("/update", methods=["PUT", "PATCH"])
def update_vacuna():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.json
            ambu = validate_vacuna_data(data)
            if VacunaModel.update_ambulancia(ambu):
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
        if request.method=="DELETE":
            affected_rows = VacunaModel.delete_vacuna(id)
            if affected_rows == 1:
                return jsonify({"message": "Vacuna Eliminada!"}), 200
            else:
                return jsonify({"message": "Vacuna  no Eliminada"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

