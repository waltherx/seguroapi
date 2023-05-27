import datetime
import random
import string
from flask import jsonify, request, Blueprint
from werkzeug.utils import secure_filename
import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary_url
from decouple import config

from models.entities.Documento import Documento

# Entities
from models.entities.Documento import Documento

# Models
from models.documentoModel import DocumentoModel

DocumentoApi = Blueprint("documento_blueprint", __name__)


@DocumentoApi.route("/<ci>")
def get_docs(ci):
    try:
        docs = DocumentoModel.get_documentos(ci)
        if docs != None:
            return jsonify({"Documentos": docs}), 200
        else:
            return (
                jsonify({"message": "nose encontro documentos con este ci :" + ci}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@DocumentoApi.route("/add", methods=["POST"])
def add_doc():
    try:
        if request.method != "POST":
            return jsonify({"message": "Método no permitido"}), 405
        tipo = request.args.get("tipo")
        id_paciente = request.args.get("id")
        # tipo = data.get("tipo")
        # id_paciente = data.get("id_paciente")
        file = request.files.get("photo")
        
        print(file.filename)

        if not all([tipo, id_paciente, file]):
            return jsonify({"message": "Se requiere el tipo, id_paciente y photo"}), 400

        cloudinary.config(
            cloud_name=config("CLOUD_NAME"),
            api_key=config("API_KEY"),
            api_secret=config("API_SECRET"),
        )

        now = datetime.datetime.now()
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=5))
        unique_str = now.strftime("%Y%m%d_%H%M%S_") + random_str
        foto_name = secure_filename(unique_str)

        upload_result = cloudinary.uploader.upload(file, public_id="doc/" + foto_name)
        foto_url = upload_result["secure_url"]
        foto_name = upload_result["public_id"]

        documento = Documento(
            None,
            foto_name,
            foto_url,
            tipo,
            None,
            now,
            id_paciente,
        )
        print(documento.to_JSON())
        insert_successful = DocumentoModel.add_documento(documento)
        if insert_successful:
            return jsonify({"message": "Imagen guardada correctamente"}), 200
        return jsonify({"message": "Error al guardar la imagen"}), 500
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@DocumentoApi.route("/view/<id>", methods=["GET"])
def view_doc(id):
    try:
        doc = DocumentoModel.view_documento(id)
        if doc != None:
            return jsonify(doc), 200
        else:
            return (
                jsonify({"message": "nose encontro documento"}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@DocumentoApi.route("/delete/<id>", methods=["DELETE"])
def delete_doc(id):
    try:
        if id:
            affected_rows = DocumentoModel.delete_documento(id)
            if affected_rows == 1:
                return jsonify({"message": "Documento eliminado exitosamente"}), 200
            else:
                return (
                    jsonify({"message": "No se encontró el Documento para eliminar"}),
                    404,
                )
        else:
            return jsonify({"message": "El ID del Documento es requerido"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@DocumentoApi.route("/update", methods=["PUT"])
def update_doc():
    pass
