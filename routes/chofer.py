from flask import Blueprint, jsonify, request

# Entities
from models.entities.Chofer import Chofer

# Models
from models.choferModel import ChoferModel

ChoferApi = Blueprint("chofer_blueprint", __name__)


@ChoferApi.route("/")
def get_chofers():
    try:
        chofers = ChoferModel.get_chofers()
        return jsonify(
            {
                "choferes": chofers,
                "message": "OK",
            }
        ), 200,
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@ChoferApi.route("/<id>")
def get_choferxId(id):
    try:
        if id:
            chofer = ChoferModel.get_chofer(id)
            return (
                jsonify(
                    {
                        "chofer": chofer,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID ambulancia"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
