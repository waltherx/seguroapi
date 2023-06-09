from flask import Blueprint, jsonify, request

# Entities
from models.entities.Persona import Persona
from models.entities.Medico import Medico
from models.entities.User import User

# Models
from models.personaModel import PersonaModel
from models.medicoModel import MedicoModel
from models.userModel import UserModel

MedicoApi = Blueprint("medico_blueprint", __name__)


@MedicoApi.route("/")
def get_medicos():
    try:
        medicos = MedicoModel.get_medicos()
        return (
            jsonify(
                {
                    "medicos": medicos,
                    "message": "OK",
                }
            ),
            200,
        )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


"""@MedicoApi.route("/view/<id>")
def view_medico(id :int):
    pass"""


@MedicoApi.route("/update",methods = ["PUT","PATCH"])
def update_medico():
    try:
        data = request.get_json()
        id = data.get("id")
        especialidad = data.get("especialidad", "")
        hospital_id = data.get("hospital_id")
        ci_persona = data.get("ci_persona")
        medico = Medico(id, especialidad, hospital_id, ci_persona)
        if MedicoModel.update_medico(medico):
            return jsonify({"message": "Medico Actualizado!"}), 200
        else:
            return jsonify({"message": "Medico no Actualizado!"}), 404
    except Exception as xx:
        return jsonify({"message": str(xx)}), 500


# medicos por hospital
@MedicoApi.route("/h/<id>")
def get_medicosxhos(id):
    try:
        medicos = MedicoModel.get_medicosXhospital(id)
        return (
            jsonify(
                {
                    "medicos": medicos,
                    "message": "OK",
                }
            ),
            200,
        )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicoApi.route("/add", methods=["POST"])
def add_medico():
    try:
        if request.method == "POST":
            # persona
            _ci_persona = request.json["ci_persona"]
            _nombre = request.json["nombres"]
            _apellido = request.json["apellidos"]
            _fecha = request.json["fecha_nacimiento"]
            _direccion = request.json["direccion"] if request.json["direccion"] else ""
            _genero = request.json["genero"]
            _estado_civil = request.json["estado_civil"]
            # medico
            _especialidad = request.json["especialidad"]
            _hospital_id = request.json["hospital_id"]
            # user
            _nameuser = request.json["nameuser"]
            _password = request.json["password"]
            _email = request.json["email"]
            print(request.json)
            new_persona = Persona(
                _ci_persona,
                _nombre,
                _apellido,
                _fecha,
                None,
                None,
                _direccion,
                _genero,
                _estado_civil,
            )
            new_medico = Medico(None, _especialidad, _hospital_id, _ci_persona)
            new_user = User(
                None, _nameuser, _password, _email, None, None, 2, _ci_persona
            )

            PersonaModel.add_persona(new_persona)
            MedicoModel.add_medico(new_medico)
            UserModel.add_user(new_user)
            return jsonify({"message": "medico agregado!"}), 200
        else:
            return jsonify({"message": "method no post"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


# medico por id
@MedicoApi.route("/view/<id>")
def get_medico_x_Id(id: int):
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
