from flask import Blueprint, jsonify, request

# Entities
from models.entities.Persona import Persona

# Models
from models.personaModel import PersonaModel

PersonaApi = Blueprint("persona_blueprint", __name__)


@PersonaApi.route("/")
def get_enfermedads():
    try:
        personas = PersonaModel.get_personas()
        return jsonify(personas)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PersonaApi.route("/<ci>")
def get_enfermedad(ci):
    try:
        persona = PersonaModel.get_persona(ci)
        if persona != None:
            return jsonify(persona)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PersonaApi.route("/add", methods=["POST"])
def add_persona():
    try:
        ci = request.json["ci"]
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        fechanac = request.json["fechanac"]
        licvehicular = request.json["licvehicular"]
        numseguro = request.json["numseguro"]
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
            numseguro,
            foto,
            tiposangre,
            hipertencion,
            altura,
            peso,
            direccion,
        )
        affected_rows = PersonaModel.add_persona(persona)
        if affected_rows == 1:
            return jsonify({"message": "insert persona"})
        else:
            return jsonify({"message": "Error on insert persona"}), 500

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PersonaApi.route("/update/<ci>", methods=["PUT"])
def update_persona(ci):
    try:
        nombres = request.json["nombres"]
        apellidos = request.json["apellidos"]
        fechanac = request.json["fechanac"]
        licvehicular = request.json["licvehicular"]
        numseguro = request.json["numseguro"]
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
            numseguro,
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


@PersonaApi.route("/delete/<id>", methods=["DELETE"])
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
