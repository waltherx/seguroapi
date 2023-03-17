from flask import Blueprint, jsonify, request

# Entities
from models.entities.Siniestro import Siniestro

# Models
from models.siniestroModel import SiniestrolModel

SiniestroApi = Blueprint("siniestro_blueprint", __name__)


@SiniestroApi.route("/")
def get_siniestros():
    try:
        siniestros = SiniestrolModel.get_siniestros()
        return jsonify(siniestros)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@SiniestroApi.route("/<id>")
def get_siniestro(id):
    try:
        siniestros = SiniestrolModel.get_siniestro(id)
        return jsonify(siniestros)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@SiniestroApi.route("/add", methods=["POST"])
def add_hospital():
    try:
        id = None
        descripccion = request.json["descripcion"]
        fecha = request.json["fecha"]        
        lat = request.json["lat"]
        long = request.json["long"]
        idper = request.json["idper"]

        siniestro = Siniestro(id, descripccion, fecha, lat, long, idper)
        affected_rows = SiniestrolModel.add_siniestro(siniestro)

        if affected_rows == 1:
            return jsonify({"message": "insert siniestro"})
        else:
            return jsonify({"message": "Error on insert siniestro"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@SiniestroApi.route("/update/<id>", methods=["PUT"])
def update_hospital(id):
    try:
        descripccion = request.json["descripccion"]
        fecha = request.json["fecha"]
        lat = request.json["lat"]
        long = request.json["long"]
        idper = request.json["idper"]

        siniestro = Siniestro(id, descripccion, fecha,  lat, long, idper)
        affected_rows = SiniestrolModel.update_siniestro(siniestro)

        if affected_rows == 1:
            return jsonify({"message": "siniestro updated"})
        else:
            return jsonify({"message": "No siniestro updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@SiniestroApi.route("/delete/<id>", methods=["DELETE"])
def delete_hospital(id):
    try:
        siniestro = Siniestro(id)
        affected_rows = SiniestrolModel.delete_hospital(siniestro)

        if affected_rows == 1:
            return jsonify(siniestro.id)
        else:
            return jsonify({"message": "No siniestro deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
