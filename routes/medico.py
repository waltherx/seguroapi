from flask import Blueprint, jsonify, request

# Entities
from models.entities.Medico import Medico

# Models
from models.medicoModel import MedicoModel

MedicoApi = Blueprint("medico_blueprint", __name__)


@MedicoApi.route("/")
def get_medicos():
    try:
        medicos = MedicoModel.get_medicos()
        return jsonify(
            {
                "medicos": medicos,
                "message": "OK",
            }
        ), 200,
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
    
@MedicoApi.route("/h/<id>")
def get_medicosxhos(id):
    try:
        medicos = MedicoModel.get_medicosXhospital(id)
        return jsonify(
            {
                "medicos": medicos,
                "message": "OK",
            }
        ), 200,
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500    

@MedicoApi.route("/view/<id>")
def get_medico_x_Id(id):
    try:
        if id:
            medico = MedicoModel.get_medico(id)
            return (
                jsonify(
                    {
                        "medico": medico,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID Medico"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500