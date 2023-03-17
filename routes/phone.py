from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Phone import Phone

# Models
from models.phoneModel import PhoneModel

PhoneApi = Blueprint("phone_blueprint", __name__)


@PhoneApi.route("/")
def get_phones():
    try:
        phones = PhoneModel.get_phones()
        return jsonify(phones)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/<id>")
def get_phone(id):
    try:
        phone = PhoneModel.get_phone(id)
        if phone != None:
            return jsonify(phone)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/add", methods=["POST"])
def add_phone():
    try:
        id = request.json["id"]
        numero = request.json["numero"]
        # id = uuid.uuid4()
        phone = Phone(id, numero)

        affected_rows = PhoneModel.add_phone(phone)

        if affected_rows == 1:
            return jsonify(phone.id)
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/update/<id>", methods=["PUT"])
def update_phone(id):
    try:
        numero = request.json["numero"]
        
        phone = Phone(id, numero)

        affected_rows = PhoneModel.update_phone(phone)

        if affected_rows == 1:
            return jsonify(phone.id)
        else:
            return jsonify({"message": "No movie updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/delete/<id>", methods=["DELETE"])
def delete_phone(id):
    try:
        phone = Phone(id)

        affected_rows = PhoneModel.delete_movie(phone)

        if affected_rows == 1:
            return jsonify(phone.id)
        else:
            return jsonify({"message": "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
