from flask import Blueprint, jsonify, request

# Entities
from models.entities.Emergencia import Emergencia

# Models
from models.emergenciaModel import EmergenciaModel

EmergenciaApi = Blueprint("emergencia_blueprint", __name__)


@EmergenciaApi.route("/<id>")
def get_docs(id):
    try:
        emergencia = EmergenciaModel.get_documentos(id)
        if emergencia != None:
            return jsonify({"Emergencia": emergencia}), 200
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
            _fecha = request.json["fecha"]
            _descripcion = request.json["descripcion"]
            _estado = request.json["estado"]
            _hospital_id = request.json["hospital_id"]
            _ambulancia_id = request.json["ambulancia_id"]
            emergencia = None
            emergencia = Emergencia(
                None, _fecha, _descripcion, _estado, _ambulancia_id, _hospital_id
            )
            if EmergenciaModel.add_emergencia(emergencia) == 1:
                return jsonify({"message": "se agrego emergencia"}), 200
            else:
                return jsonify({"message": "ERROR agregar emergencia"}), 404
    return (
        jsonify({"message": "error no http POST"}),
        404,
    )
