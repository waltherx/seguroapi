from flask import Blueprint, jsonify, request

# Entities
from models.entities.Emergencia import Emergencia

# Models
from models.emergenciaModel import EmergenciaModel

EmergenciaApi = Blueprint("emergencia_blueprint", __name__)

@EmergenciaApi.route("/")
def get_all_emgergencias():
    try:
        emergencias = EmergenciaModel.get_emergencias()
        if emergencias != None:
            return jsonify(emergencias), 200
        else:
            return (
                jsonify({"message": "nose encontro emergencias"}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@EmergenciaApi.route("/<id>")
def get_emgergencias(id):
    try:
        emergencia = EmergenciaModel.get_emergencia(id)
        if emergencia != None:
            return jsonify({"Emergencia": emergencia, "message": "OK"}), 200
        else:
            return (
                jsonify({"message": "nose encontro la emergencia con id :" + id}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@EmergenciaApi.route("/add", methods=["POST"])
def add_emergencia():
    if request.method == "POST":
        _descripcion = request.json["descripcion"]
        _estado = request.json["estado"]
        _hospital_id = request.json["hospital_id"]
        _ambulancia_id = request.json["ambulancia_id"]
        emergencia = None
        emergencia = Emergencia(
            None, None, _descripcion, _estado, _ambulancia_id, _hospital_id
        )
        if EmergenciaModel.add_emergencia(emergencia) == 1:
            return jsonify({"message": "se agrego emergencia"}), 200
        else:
            return jsonify({"message": "ERROR agregar emergencia"}), 404
    return (
        jsonify({"message": "error no http POST"}),
        404,
    )


@EmergenciaApi.route("/update/e/", methods=["PUT", "PACTH"])
def update_emergencia():
    if request.method == "PUT" or request.method == "PATCH":
        _id = request.json["id"]
        _estado = request.json["estado"]
        emergencia = None
        emergencia = Emergencia(_id, None, None, _estado, None, None)
        if EmergenciaModel.update_emergencia(emergencia) == 1:
            return jsonify({"message": "se actualizo el estado de emergencia"}), 200
        else:
            return jsonify({"message": "ERROR No Update emergencia"}), 404
    return (
        jsonify({"message": "error no http PUT or Path"}),
        404,
    )
