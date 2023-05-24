from flask import Blueprint, jsonify, request

# Entities
from models.entities.Persona import Persona
from models.entities.Paciente import Paciente
from models.entities.User import User

# Models
from models.phoneModel import PhoneModel
from models.medicamentoModel import MedicamentoModel
from models.vacunaModel import VacunaModel
from models.operacionModel import OperacionModel

from models.personaModel import PersonaModel
from models.pacienteModel import PacienteModel
from models.userModel import UserModel

PacienteApi = Blueprint("paciente_blueprint", __name__)


@PacienteApi.route("/")
def get_personas():
    try:
        personas = PersonaModel.get_personas()
        return jsonify(personas)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PacienteApi.route("/<ci>")
def get_persona56(ci):
    try:
        if ci:
            persona = PersonaModel.get_persona(ci)
            vacunas = VacunaModel.get_vacuna(ci)
            operacions = VacunaModel.get_vacuna(ci)
            medicamentos = VacunaModel.get_vacuna(ci)
            phones = PhoneModel.get_phone(ci)
            return (
                jsonify(
                    {
                        "Paciente": persona,
                        "Vacunas": vacunas,
                        "Operaciones": operacions,
                        "Medicamentos": medicamentos,
                        "Telefonos": phones,
                        "message": "OK",
                    }
                ),
                200,
            )
        return jsonify({"message": "falta el valor CI de Paciente"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PacienteApi.route("/p/<ci>", methods=["GET"])
def get_paramed_xci(ci):
    try:
        if ci:
            paciente = PacienteModel.get_paciente_X_ci(ci)
            return (jsonify({"data": paciente, "message": "OK"}), 200)
        return jsonify({"message": "falta el valor ID Paciente"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PacienteApi.route("/add", methods=["POST"])
def add_paciente():
    try:
        if request.method == "POST":
            _ci_persona = request.json["ci_persona"]
            _nombre = request.json["nombres"]
            _apellido = request.json["apellidos"]
            _fecha = request.json["fecha_nacimiento"]
            _direccion = request.json["direccion"] if request.json["direccion"] else ""
            _genero = request.json["genero"]
            _estado_civil = request.json["estado_civil"]
            # paciente
            _tipo_sangre = request.json["tipo_sangre"]
            _hipertencion = request.json["hipertencion"]
            _altura = request.json["altura"]
            _peso = request.json["peso"]
            # user
            _nameuser = request.json["nameuser"]
            _password = request.json["password"]
            _email = request.json["email"]
            x = 'paciente'
            print(f'>{x:=^22}<')
            print(request.json)
            print(f'>{x:=^22}<')
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
            new_paciente = Paciente(
                None, _tipo_sangre, _hipertencion, _altura, _peso, _ci_persona
            )
            new_user = User(
                None, _nameuser, _password, _email, None, None, 5, _ci_persona
            )

            PersonaModel.add_persona(new_persona)
            PacienteModel.add_paciente(new_paciente)
            UserModel.add_user(new_user)
            return jsonify({"message": "Paciente agregado!"}), 200
        else:
            return jsonify({"message": "method no post"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PacienteApi.route("/update/<ci>", methods=["PUT"])
def update_persona(ci):
    try:
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        fechanac = request.json["fechanac"]
        licvehicular = request.json["licvehicular"]
        foto = request.json["foto"]
        tiposangre = request.json["tiposangre"]
        hipertencion = request.json["hipertencion"]
        altura = request.json["altura"]
        peso = request.json["peso"]
        direccion = request.json["direccion"]
        persona = Persona(
            ci,
            nombres,
            apellidos,
            fechanac,
            licvehicular,
            foto,
            tiposangre,
            hipertencion,
            altura,
            peso,
            direccion,
        )
        affected_rows = PersonaModel.update_persona(persona)

        if affected_rows == 1:
            return jsonify({"message": "persona updated"})
        else:
            return jsonify({"message": "No persona updated"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PacienteApi.route("/delete/<id>", methods=["DELETE"])
def delete_persona(ci):
    try:
        persona = Persona(ci)
        affected_rows = PersonaModel.delete_persona(persona)

        if affected_rows == 1:
            return jsonify({"message": "enfermedad deleted"})
        else:
            return jsonify({"message": "No enfermedad deleted"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
