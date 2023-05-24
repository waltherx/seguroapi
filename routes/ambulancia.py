from flask import Blueprint, jsonify, request

# Entities
from models.entities.Chofer import Chofer
from models.entities.Paramedico import Paramedico
from models.entities.Ambulancia import Ambulancia

# Models
from models.paramedicoModel import ParamedicoModel
from models.choferModel import ChoferModel
from models.ambulanciaModel import AmbulanciaModel
from models.emergenciaModel import EmergenciaModel

AmbulanciaApi = Blueprint("ambulancia_blueprint", __name__)


@AmbulanciaApi.route("/")
def get_ambulancias():
    try:
        ambulancias = AmbulanciaModel.get_ambulancia()
        return jsonify(ambulancias)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/<id>")
def get_ambulanciaxId(id):
    try:
        if id:
            chofers = ChoferModel.get_chofersxId(id)
            paramedicos = ParamedicoModel.get_paramedicos(id)
            ambulancia = AmbulanciaModel.get_ambulanciaId(id)
            return (
                jsonify(
                    {
                        "ambulancia": ambulancia,
                        "choferes": chofers,
                        "Paramedicos": paramedicos,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor ID ambulancia"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/e/<id>", methods=["GET"])
def get_Emergencia(id):
    try:
        if id:
            emergencias = EmergenciaModel.get_emergencias_x_ambulancia(id)
            return jsonify({"emergencias": emergencias, "message": "OK"}), 200
        return jsonify({"message": "falta el valor ID ambulancia"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/location", methods=["PUT", "PATCH"])
def update_location():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            _id = request.json["id"]
            _lat = request.json["lat"]
            _lng = request.json["lng"]
            ambu = Ambulancia(_id, None, None, None, None, None, _lat, _lng, None)
            if AmbulanciaModel.update_location(ambu):
                return jsonify({"message": "Posicion Actualizada"}), 200
            else:
                return jsonify({"message": "Posicion no Actualizada"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/add", methods=["POST"])
def add_ambulancia():
    try:
        if request.method == "POST":
            data = request.json
            _modelo = data["modelo"]
            _marca = data["marca"]
            _anio = data["anio"]
            _placa = data["placa"]
            _capacidad = data["capacidad"]
            ambu = Ambulancia(
                None, _modelo, _marca, _anio, _placa, _capacidad, None, None, None
            )
            if AmbulanciaModel.add_ambulancia(ambu):
                return jsonify({"message": "Ambulnacia Agregada!"}), 200
            else:
                return jsonify({"message": "Ambulnacia no Agregada!"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/update", methods=["PUT", "PATCH"])
def update_ambulancia():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.json
            _id = data["id"]
            _modelo = data["modelo"]
            _marca = data["marca"]
            _anio = data["anio"]
            _placa = data["placa"]
            _capacidad = data["capacidad"]
            ambu = Ambulancia(
                _id, _modelo, _marca, _anio, _placa, _capacidad, None, None, None
            )
            if AmbulanciaModel.update_ambulancia(ambu):
                return jsonify({"message": "Ambulnacia Actualizada!"}), 200
            else:
                return jsonify({"message": "Ambulnacia no Actualizada!"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@AmbulanciaApi.route("/location/ambulancia/<id>", methods=["PUT"])
def update_state_ambulancia():
    pass


@AmbulanciaApi.route("/ch/<id>", methods=["GET"])
def get_ambulancia_choferid(id):
    try:
        if request.method == "GET":
            if id:
                ambulancias = AmbulanciaModel.get_ambulanciaIdchofer(id)
                return jsonify({"ambulancias": ambulancias, "message": "OK"}), 200
            return jsonify({"message": "falta el valor ID ambulancia"}), 500
        return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
