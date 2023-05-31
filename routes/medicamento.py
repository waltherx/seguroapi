from flask import Blueprint, jsonify, request

# Entities
from models.entities.Medicamento import Medicamento

# Models
from models.medicamentoModel import MedicamentoModel

MedicamentoApi = Blueprint("medicamento_blueprint", __name__)


@MedicamentoApi.route("/<ci>")
def get_medicamento(ci):
    try:
        medicamento = MedicamentoModel.get_medicamento(ci)
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

@MedicamentoApi.route("/view/<id>", methods=["GET"])
def view_medicam(id):
    try:
        if request.method == "GET":
            medicam = MedicamentoModel.view_medicamentos(id)
            if medicam is not None:
                return jsonify(medicam), 200
            else:
                return jsonify({"message": "no se encontro Medicamento!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@MedicamentoApi.route("/update/<id>", methods=["PUT"])
def update_hospital(id):
    try:
        nombre = request.json["nombre"]
        direccion = request.json["direccion"]
        lat = request.json["lat"]
        long = request.json["long"]
        medicam = Medicamento(id, nombre, direccion, lat, long)
        affected_rows = MedicamentoModel.update_medicamento(medicam)
        if affected_rows == 1:
            return jsonify({"message": "medicamento updated"})
        else:
            return jsonify({"message": "No medicamento updated"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/delete/<id>", methods=["DELETE"])
def delete_hospital(id):
    try:
        if request.method=="DELETE":
            affected_rows = MedicamentoModel.delete_medicamento(id)
            if affected_rows == 1:
                return jsonify({"message": "Medicamento Eliminado!"}), 404
            else:
                return jsonify({"message": "Medicamento no Eliminado!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
