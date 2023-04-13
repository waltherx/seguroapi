from flask import Flask
from flask import Blueprint
from flask import render_template, flash, request, redirect
from decouple import config
from models.entities.Documento import Documento
from models.documentoModel import DocumentoModel

from models.personaModel import PersonaModel
from models.vacunaModel import VacunaModel
from models.operacionModel import OperacionModel
from models.documentoModel import DocumentoModel
from models.medicamentoModel import MedicamentoModel
from models.phoneModel import PhoneModel

import datetime, time
from werkzeug.utils import secure_filename
import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary

documentoWeb = Blueprint(
    "documento_bp", __name__, template_folder="templates/documento"
)

@documentoWeb.route("/<ci>",methods=["GET"])
def get_docs(ci):
    pass


@documentoWeb.route("/create/<ci>", methods=["POST"])
def add_document(ci):
    if request.method == "POST":
        _tipo = request.args.get("txtTipo")
        _fecha = datetime.datetime.now()
        timeFormat = _fecha.strftime("%d/%m/%Y %H:%M:%S")
        _feha = timeFormat
        _documento = request.files["txtDoc"]
        _nameDoc = _documento.filename
        _descripcion = request.args.get("txtDescrip")
        cloudinary.config(
            cloud_name=config("CLOUD_NAME"),
            api_key=config("API_KEY"),
            api_secret=config("API_SECRET"),
        )
        epoch_time = int(time.time())
        fileName = secure_filename(str(epoch_time) + "-" + _nameDoc)
        upload_result = None
        if _documento:
            upload_result = cloudinary.uploader.upload(
                _documento, public_id="doc/" + fileName
            )
            _url = upload_result["secure_url"]
            _docu = Documento(None, _url, _tipo, _descripcion, ci)
            flash("Documento subido.." + fileName)
            personaOne = PersonaModel.get_persona(id)
            vacunaList = VacunaModel.get_vacuna(id)
            operacionList = OperacionModel.get_operacion(id)
            medicamentoList = MedicamentoModel.get_medicamento(id)
            phonesList = PhoneModel.get_phone(id)
            docList = DocumentoModel.get_documentos(id)
            return render_template(
                "persona/modal/view.html",
                paciente=personaOne,
                phones=phonesList,
                vacunas=vacunaList,
                operaciones=operacionList,
                medicamentos=medicamentoList,
                documentos=docList
            )
    return redirect("/enfermedad")
