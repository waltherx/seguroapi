from flask import Flask
from flask import Blueprint
from flask import (
    render_template,
    redirect,
    request,
    flash,
)
import os
import boto3
from models.entities.Persona import Persona
from models.personaModel import PersonaModel
from models.vacunaModel import VacunaModel
from models.operacionModel import OperacionModel
from models.documentoModel import DocumentoModel
from models.medicamentoModel import MedicamentoModel

from models.phoneModel import PhoneModel
from werkzeug.utils import secure_filename
from decouple import config
from database.s3_functions import upload_file, show_image

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
BUCKET = "bucketeer-d4a26368-c4f6-4ca8-8a04-a86479106124"
KEY_BUCKET = "AKIAVVKH7VVUPMQIKXWX"
AWS_SECRET_KEY = "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"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


personaweb = Blueprint("persona_bp", __name__, template_folder="templates/persona")


# @login_required
@personaweb.route("/")
def index():
    personaList = PersonaModel.get_personas()
    return render_template("/persona/index.html", personas=personaList)


@personaweb.route("/view/<id>", methods=["GET", "POST"])
def view(id):
    personaOne = PersonaModel.get_persona(id)
    vacunaList = VacunaModel.get_vacuna(id)
    operacionList = OperacionModel.get_operacion(id)
    medicamentoList = MedicamentoModel.get_medicamento(id)
    phonesList = PhoneModel.get_phone(id)
    return render_template(
        "persona/modal/view.html",
        paciente=personaOne,
        phones=phonesList,
        vacunas=vacunaList,
        operaciones=operacionList,
        medicamentos=medicamentoList
    )


@personaweb.route("/createp", methods=["GET"])
def createp():
    return render_template("persona/modal/create.html")


@personaweb.route("/updatep/<ci>", methods=["GET"])
def updatep(ci):
    persona = PersonaModel.get_persona(ci)
    return render_template("persona/modal/edit.html", paciente=persona)


# @login_required
@personaweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        _ci = request.form.get("txtCI")
        _nombre = request.form.get("txtNombre")
        _apellido = request.form.get("txtApellido")
        _fecha = request.form.get("txtFecha")
        _lic = request.form.get("txtLicVe")
        _foto = request.files.get("txtFoto")
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
				_altura,
				_peso,
				_direccion,
			)
		"""
        cwd = os.getcwd()
        if not os.path.isdir("TEMPDIR"):
            os.mkdir("TEMPDIR")
        if "txtFoto" not in request.files:
            return "No user_file key in request.files"
            file = request.files["txtFoto"]
            # There is no file selected to upload
        if _foto.filename == "":
            return "Please select a file"

        if _foto and allowed_file(_foto.filename):
            img_name = secure_filename(_foto.filename)
            filepath = cwd + "\\TEMPDIR\\" + img_name
            _foto.save(filepath)
            s3_client = boto3.client(
                "s3", aws_access_key_id=KEY_BUCKET, aws_secret_access_key=AWS_SECRET_KEY
            )
            s3_client.upload_file(filepath, BUCKET, img_name)
            os.remove(filepath)
            flash("File Upload Succesful")
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


# @login_required
@personaweb.route("/update/<id>", methods=["GET", "POST"])
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
def delete(id):
    enfermedad = Persona(id, "Elimina")
    PersonaModel.delete_persona(enfermedad)
    return redirect("/paciente")
