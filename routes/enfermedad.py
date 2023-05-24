from flask import Blueprint, jsonify, request

# Entities
from models.entities.Enfermedad import Enfermedad

# Models
from models.enfermedadModel import EnfermedadModel

EnfermedadApi = Blueprint("enfermedad_blueprint", __name__)


@EnfermedadApi.route("/")
def get_enfermedads():
    try:
        enfermedads = EnfermedadModel.get_enfermedads()
        return jsonify(enfermedads)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/<ci>")
def get_enfermedad(ci):
    try:
        enfermedad = EnfermedadModel.get_enfermedad(ci)
        if enfermedad != None:
            return jsonify(enfermedad)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/add", methods=["POST"])
def add_enfermedad():
    try:
        id = None
        nombre = request.json["nombre"]
        enfermedad = Enfermedad(id, nombre)
        affected_rows = EnfermedadModel.add_enfermedad(enfermedad)        
        if affected_rows == 1:
            return jsonify({"message": "insert enfermedad"})
        else:
            return jsonify({"message": "Error on insert"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/update/<id>", methods=["PUT"])
def update_enfermedad(id):
    try:
        nombre = request.json["nombre"]
        enfermedad = Enfermedad(id, nombre)
        affected_rows = EnfermedadModel.update_enfermedad(enfermedad)

        if affected_rows == 1:
            return jsonify({"message": "enfermedad updated"})
        else:
            return jsonify({"message": "No enfermedad updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EnfermedadApi.route("/delete/<id>", methods=["DELETE"])
def delete_enfermedad(id):
    try:        
        enfermedad = Enfermedad(id)
        affected_rows = EnfermedadModel.delete_enfermedad(enfermedad)

        if affected_rows == 1:
            return jsonify({"message": "enfermedad deleted"})
        else:
            return jsonify({"message": "No enfermedad deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
