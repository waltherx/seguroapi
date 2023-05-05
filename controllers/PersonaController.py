import os
import logging
from flask_login import login_required
from flask import Blueprint
from flask import render_template, redirect, request, flash, jsonify

import cloudinary
from cloudinary import uploader, api
from cloudinary.utils import cloudinary_url
from models.entities.Persona import Persona
from models.personaModel import PersonaModel
from models.vacunaModel import VacunaModel
from models.operacionModel import OperacionModel
from models.documentoModel import DocumentoModel
from models.medicamentoModel import MedicamentoModel
from models.phoneModel import PhoneModel
from models.documentoModel import DocumentoModel

from werkzeug.utils import secure_filename
from decouple import config


# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


personaweb = Blueprint("persona_bp", __name__, template_folder="templates/persona")


@personaweb.route("/")
@login_required
def index():
    personaList = PersonaModel.get_personas()
    return render_template("/persona/index.html", personas=personaList)


@personaweb.route("/view/<id>", methods=["GET", "POST"])
@login_required
def view(id):
    personaOne = PersonaModel.get_persona(id)
    vacunaList = VacunaModel.get_vacuna(id)
    operacionList = OperacionModel.get_operacion(id)
    medicamentoList = MedicamentoModel.get_medicamento(id)
    phonesList = PhoneModel.get_phone(id)
    docList = DocumentoModel.get_documentos(id)
    return render_template(
        "persona/modal/view2.html",
        paciente=personaOne,
        phones=phonesList,
        vacunas=vacunaList,
        operaciones=operacionList,
        medicamentos=medicamentoList,
        documentos=docList,
    )


@personaweb.route("/createp", methods=["GET"])
@login_required
def createp():
    return render_template("persona/modal/create.html")


@personaweb.route("/updatep/<ci>", methods=["GET"])
@login_required
def updatep(ci):
    persona = PersonaModel.get_persona(ci)
    return render_template("persona/modal/edit.html", paciente=persona)


# @login_required
@personaweb.route("/create", methods=["POST"])
@login_required
def create():
    if request.method == "POST":
        _ci = request.form.get("txtCI")
        _nombre = request.form.get("txtNombre")
        _apellido = request.form.get("txtApellido")
        _fecha = request.form.get("txtFecha")
        _lic = request.form.get("txtLicVe")
        # _foto = request.files.get("txtFoto")
        """
		_sangre = request.form.get("txtSangre")
		_hiper = request.form.get("txtHipertencion")
		_altura = request.form.get("txtAltura")
		_peso = request.form.get("txtPeso")
		_direccion = request.form.get("txtDireccion")		
		try:
			persona = Persona(
				_ci,
				_nombre,
				_apellido,
				_fecha,
				0,
				img_name,
				_sangre,
				_hiper,
			S	_altura,
				_peso,
				_direccion,
			)
		"""
        cloudinary.config(
            cloud_name=config("CLOUD_NAME"),
            api_key=config("API_KEY"),
            api_secret=config("API_SECRET"),
        )
        upload_result = None
        if request.method == "POST":
            file_to_upload = request.files["txtFoto"]
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(file_to_upload)
            return redirect("/paciente")

        return redirect("/paciente")
        """affected_rows = PersonaModel.add_persona(persona)
			if affected_rows == 1:
				flash("Persona Agregada!")
				return redirect("/paciente")
			else:
				flash("Persona no Agregada")
				return redirect("/paciente")
		except Exception as e:
			flash(e.args[1])
			return redirect("/paciente")"""


@personaweb.route("/update/<id>", methods=["GET", "POST"])
@login_required
def update(id):
    if request.method == "POST":
        _nombre = request.form.get("nombre")
        try:
            persona = Persona(id, _nombre)
            PersonaModel.update_persona(persona)
            flash("Persona Updated Successfully")
            return redirect("/paciente")
        except Exception as e:
            flash(e.args[1])
            return redirect("/paciente")


@personaweb.route("/delete/<id>", methods=["GET", "POST"])
@login_required
def delete(id):
    enfermedad = Persona(id, "Elimina")
    PersonaModel.delete_persona(enfermedad)
    return redirect("/paciente")
