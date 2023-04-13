from flask import Blueprint, jsonify, request

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
