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

personaweb = Blueprint(
    "persona_bp", __name__, template_folder="templates/persona"
)


# @login_required
@personaweb.route("/")
def index():
    personaList = PersonaModel.get_personas()
    return render_template("/persona/index.html", personas=personaList)


# @login_required
@personaweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        _nombre = request.form["txtNombre"]
        try:
            persona = Persona(None, _nombre)
            PersonaModel.add_persona(persona)
            flash("Persona Agregada successfully")
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
