from flask import Blueprint, jsonify, request

# Entities
from models.entities.Token import Token

# Models
from models.tokenModel import TokenModel

TokenApi = Blueprint("token_blueprint", __name__)


@TokenApi.route("/add", methods=["POST"])
def add_alergia():
    try:
        id = None
        _token = request.json["token"]
        _user_name = request.json["user_id"]
        token = Token(id, _user_name, _token, None, None)
        affected_rows = TokenModel.add_token(token)

        if affected_rows == 1:
            return jsonify({"message": "Token insert!"}), 201
        else:
            return jsonify({"message": "Error on insert"})
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@TokenApi.route("/delete/<id>", methods=["DELETE"])
def delete_alergia(id):
    try:
        affected_rows = TokenModel.delete_token(id)
        if affected_rows == 1:
            return jsonify({"message": "token deleted"}), 200
        else:
            return jsonify({"message": "token deleted"})

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
