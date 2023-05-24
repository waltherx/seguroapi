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