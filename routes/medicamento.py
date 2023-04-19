from flask import Blueprint, jsonify, request

# Entities
from models.entities.Medicamento import Medicamento

# Models
from models.medicamentoModel import MedicamentoModel

MedicamentoApi = Blueprint("medicamento_blueprint", __name__)


@MedicamentoApi.route("/<id>")
def get_medicamento(id):
    try:
        medicamento = MedicamentoModel.get_medicamento(id)
        if medicamento != None:
            return jsonify(medicamento), 200
        else:
            return jsonify({"msg": "az"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/add", methods=["POST"])
def add_hospital():
    try:
        id = None
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]
        medicamento = Medicamento(id, nombre, direccion, lat, long)
        affected_rows = MedicamentoModel.add_medicamento(medicamento)
        if affected_rows == 1:
            return jsonify({"message": "insert medicamento"})
        else:
            return jsonify({"message": "Error on insert medicamento"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/update/<id>", methods=["PUT"])
def update_hospital(id):
    try:
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]
        alergia = Medicamento(id, nombre, direccion, lat, long)
        affected_rows = MedicamentoModel.update_medicamento(alergia)
        if affected_rows == 1:
            return jsonify({"message": "medicamento updated"})
        else:
            return jsonify({"message": "No medicamento updated"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/delete/<id>", methods=["DELETE"])
def delete_hospital(id):
    try:
        hospital = Medicamento(id)
        affected_rows = MedicamentoModel.delete_hospital(hospital)
        if affected_rows == 1:
            return jsonify(hospital.id)
        else:
            return jsonify({"message": "No medicamento deleted"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
