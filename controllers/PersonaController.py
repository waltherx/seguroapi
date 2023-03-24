from flask import Flask
from flask import Blueprint
from flask import (
    config,
    render_template,
    redirect,
    url_for,
    request,
    abort,
    flash,
)
from models.entities.Persona import Persona
from models.personaModel import PersonaModel
from models.phoneModel import PhoneModel
import os
from werkzeug.utils import secure_filename
from decouple import config

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


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
    phonesList = PhoneModel.get_phone(id)
    return render_template(
        "persona/modal/view.html", paciente=personaOne, phones=phonesList
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
        _sangre = request.form.get("txtSangre")
        _hiper = request.form.get("txtHipertencion")
        _altura = request.form.get("txtAltura")
        _peso = request.form.get("txtPeso")
        _direccion = request.form.get("txtDireccion")
        img_name = secure_filename(_foto.filename)
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
            saved_path = os.path.join(config("UPLOAD_FOLDER"), img_name)
            _foto.save(saved_path)
            print(saved_path)
            affected_rows = PersonaModel.add_persona(persona)
            if affected_rows == 1:
                flash("Persona Agregada!")
                return redirect("/paciente")
            else:
                flash("Persona no Agregada")
                return redirect("/paciente")
        except Exception as e:
            flash(e.args[1])
            return redirect("/paciente")


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
