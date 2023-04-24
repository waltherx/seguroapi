from flask import Blueprint, jsonify, request

# Entities
from models.entities.Persona import Persona

# Models
from models.phoneModel import PhoneModel
from models.medicamentoModel import MedicamentoModel
from models.vacunaModel import VacunaModel
from models.operacionModel import OperacionModel

from models.personaModel import PersonaModel
from models.pacienteModel import PacienteModel

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
def add_persona():
    try:
        ci = request.json["ci"]
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
        ci_persona = PersonaModel.add_persona(persona)
        if ci_persona != 0:
            return jsonify({"ci": ci_persona, "message": "Paciente agregado"})
        else:
            return jsonify({"message": "Error on insert persona"}), 500

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
