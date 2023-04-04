from flask import Blueprint, jsonify, request

# Entities
from models.entities.Chofer import Chofer
from models.entities.Paramedico import Paramedico
from models.entities.Ambulancia import Ambulancia

# Models
from models.paramedicoModel import ParamedicoModel
from models.choferModel import ChoferModel
from models.ambulanciaModel import AmbulanciaModel

AmbulanciaApi = Blueprint("ambulancia_blueprint", __name__)


@AmbulanciaApi.route("/")
def get_ambulancias():
    try:
        ambulancias = AmbulanciaModel.get_ambulancia()
        return jsonify(ambulancias)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/<id>")
def get_ambulancia56(id):
    try:
        if id:
            chofers = ChoferModel.get_chofers(id)
            paramedicos = ParamedicoModel.get_paramedicos(id)
            ambulancia = AmbulanciaModel.get_ambulanciaId(id)
            return (
                jsonify(
                    {
                        "ambulancia": ambulancia,
                        "choferes": chofers,
                        "Paramedicos": paramedicos,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID ambulancia"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
