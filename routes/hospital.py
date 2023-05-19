from flask import Blueprint, jsonify, request

# Entities
from models.entities.Hospital import Hospital
from models.entities.Medico import Medico

# Models
from models.hospitalModel import HospitalModel
from models.medicoModel import MedicoModel

HospitalApi = Blueprint("hospital_blueprint", __name__)


@HospitalApi.route("/")
def get_hospitals():
    try:
        hospitals = HospitalModel.get_hospitals()
        return jsonify(hospitals)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@HospitalApi.route("/<id>")
def get_hospital(id):
    try:
        hospital = HospitalModel.get_hospital(id)
        medicos = MedicoModel.get_medicosXhospital(id)
        if hospital != None:
            return (
                jsonify({"hospital": hospital, "medicos": medicos, "message": "ok"}),
                200,
            )
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@HospitalApi.route("/add", methods=["POST"])
def add_hospital():
    try:
        id = None
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]

        hospital = Hospital(id, nombre, direccion, lat, long)
        affected_rows = HospitalModel.add_hospital(hospital)

        if affected_rows == 1:
            return jsonify({"message": "insert hospital"})
        else:
            return jsonify({"message": "Error on insert hospital"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@HospitalApi.route("/update/<id>", methods=["PUT"])
def update_hospital(id):
    try:
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]

        alergia = Hospital(id, nombre, direccion, lat, long)
        affected_rows = HospitalModel.update_hospital(alergia)

        if affected_rows == 1:
            return jsonify({"message": "hospital updated"})
        else:
            return jsonify({"message": "No hospital updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@HospitalApi.route("/delete/<id>", methods=["DELETE"])
def delete_hospital(id):
    try:
        hospital = Hospital(id)

        affected_rows = HospitalModel.delete_hospital(hospital)

        if affected_rows == 1:
            return jsonify(hospital.id)
        else:
            return jsonify({"message": "No hospital deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@HospitalApi.route("/geojson", methods=["GET"])
def hospital_geojson():
    try:
        features = []
        hospitals = HospitalModel.get_hospitals()
        for row in hospitals:
            feature = {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [row["long"], row["lat"]]},
                "properties": {"name": row["nombre"], "description": row["direccion"]},
            }
            features.append(feature)
        return jsonify({"type": "FeatureCollection", "features": features}), 200
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
