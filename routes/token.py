from flask import Blueprint, jsonify, request

# Entities
from models.entities.Token import Token

# Models
from models.tokenModel import TokenModel

TokenApi = Blueprint("token_blueprint", __name__)


@TokenApi.route("/<id>", methods=["GET"])
def get_token(id):
    try:
        _tokens = TokenModel.get_token(id)
        if _tokens != None:
            return jsonify({"tokens": _tokens})
        return jsonify({"message": "no hay tokens"})
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@TokenApi.route("/add", methods=["POST"])
def add_token():
    try:
        id = None
        _token = request.json["token"]
        _user_name = request.json["user_id"]
        token = Token(id, _user_name, _token, None, None)
        res_token = TokenModel.add_token(token)

        if res_token != None:
            return jsonify({"id_token": res_token, "message": "token insertado!"}), 201
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
