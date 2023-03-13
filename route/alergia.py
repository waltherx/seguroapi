from flask import Blueprint, jsonify, request

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


@AlergiaApi.route("/<id>")
def get_alergia(id):
    try:
        alergia = AlergiaModel.get_alergia(id)
        if alergia != None:
            return jsonify(alergia)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/add", methods=["POST"])
def add_alergia():
    try:
        id = None
        nomnbre = request.json["nomnbre"]
        alergia = Alergia(id, nomnbre)
        affected_rows = AlergiaModel.add_alergia(alergia)

        if affected_rows == 1:
            return jsonify(alergia.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AlergiaApi.route("/update/<id>", methods=["PUT"])
def update_alergia(id):
    try:
        nombre = request.json["nombre"]

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
        alergia = Alergia(id)

        affected_rows = AlergiaModel.delete_alergia(alergia)

        if affected_rows == 1:
            return jsonify(alergia.id)
        else:
            return jsonify({"message": "No alergia deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
