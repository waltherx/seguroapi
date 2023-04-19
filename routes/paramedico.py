from flask import Blueprint, jsonify, request

# Entities
from models.entities.Paramedico import Paramedico

# Models
from models.paramedicoModel import ParamedicoModel

ParamedicoApi = Blueprint("paramedico_blueprint", __name__)


@ParamedicoApi.route("/<id>",  methods=["GET"])
def get_paramedicos(id):
    try:
        paramedicos = ParamedicoModel.get_paramedicos(id)
        return (
            jsonify(
                {
                    "paramedicos": paramedicos,
                    "message": "OK",
                }
            ),
            200,
        )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@ParamedicoApi.route("/view/<id>")
def get_paramedico_by_id(id):
    try:
        if id:
            paramedico = ParamedicoModel.get_paramedico(id)
            return (
                jsonify(
                    {
                        "paramedico": paramedico,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID Paramedico"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
