from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest
import datetime
import random
import string
import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary_url
from decouple import config


# Entities
from models.entities.Persona import Persona

# Models
from models.personaModel import PersonaModel

PersonaApi = Blueprint("prna_blueprint", __name__)


@PersonaApi.route("/view/<ci>", methods=["GET"])
def view_persona(ci: int):
    try:
        if request.method == "GET":
            person = PersonaModel.view_persona(ci)
            if person:
                return jsonify(person), 200
            else:
               return jsonify({"message": "no encontrado"}), 404
        return jsonify({"message": "Metodo http incorrecto"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_persona(data):
    required_fields = ["ci", "nombres", "apellidos"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
    ci = data["ci"]
    nombres = data.get("nombres", "")
    apellidos = data.get("apellidos", "")
    fecha_nacimiento = data.get("fecha_nacimiento", "")
    direccion = data.get("direccion", "")
    genero = data.get("genero")
    estado_civil = data.get("estado_civil")

    return Persona(
        ci,
        nombres,
        apellidos,
        fecha_nacimiento,
        None,
        None,
        direccion,
        genero,
        estado_civil,
    )


@PersonaApi.route("/update", methods=["PUT", "PATCH"])
def update_persona():
    try:
        if request.method == "PUT" or request.method == "PACTH":
            data = request.get_json()
            person = validate_persona(data)
            affected_row = PersonaModel.update_persona(person)
            if affected_row == 1:
                person = PersonaModel.view_persona(person.ci)
                return jsonify(person), 200
            else:
                return jsonify({"message": "Persona no Actualizada"}), 404
        return jsonify({"message": "Metodo http incorrecto"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PersonaApi.route("/upload/<ci>", methods=["POST"])
def upload_perfil(ci):
    try:
        if ci:
            if request.method == "POST":
                file = request.files["photo"]
                if file:
                    cloudinary.config(
                        cloud_name=config("CLOUD_NAME"),
                        api_key=config("API_KEY"),
                        api_secret=config("API_SECRET"),
                    )
                    now = datetime.datetime.now()
                    random_str = "".join(
                        random.choices(string.ascii_letters + string.digits, k=5)
                    )
                    unique_str = now.strftime("%Y%m%d_%H%M%S_") + random_str
                    foto_name = secure_filename(str(unique_str))
                    upload_result = cloudinary.uploader.upload(
                        file, public_id="photo/" + foto_name
                    )
                    foto_url = upload_result["secure_url"]
                    foto_name = foto_name + "." + upload_result["format"]
                    per = Persona(
                        ci, None, None, None, foto_url, foto_name, None, None, None
                    )
                    PersonaModel.upload_photo(per)
                    return jsonify({"message": "Imagen guardado correctamente"}), 200
                return jsonify({"message": "No se ha podido guardar el Imagen"}), 400
            else:
                return jsonify({"message": "Metodo no permitido"}), 400
        else:
            return jsonify({"message": "Metodo no permitido"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
