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

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

personaweb = Blueprint("persona_bp", __name__, template_folder="templates/persona")


# @login_required
@personaweb.route("/")
def index():
    personaList = PersonaModel.get_personas()
    return render_template("/persona/index.html", personas=personaList)


@personaweb.route("/view/<id>", methods=["GET", "POST"])
def view(id):
    personaVw = PersonaModel.get_persona(id)
    return render_template("persona/modal/view.html", paciente=personaVw)


@personaweb.route("/createp", methods=["GET"])
def createp():
    return render_template("persona/modal/create.html")


# @login_required
@personaweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        _ci = request.form.get("txtCI")
        _nombre = request.form.get("txtNombre")
        _apellido = request.form.get("txtApellido")
        _fecha = request.form.get("txtFecha")
        # tipo = json_args['tipo'] if 'tipo' in request.json else None
        _lic = request.form.get("txtLicVe")
        _foto = request.form.get("txtFoto")
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
                _foto,
                _sangre,
                _hiper,
                _altura,
                _peso,
                _direccion,
            )
            print(persona.to_JSON())
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
            enfermedad = Persona(id, _nombre)
            PersonaModel.update_persona(enfermedad)
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
