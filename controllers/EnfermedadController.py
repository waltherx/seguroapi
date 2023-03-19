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
from models.entities.Enfermedad import Enfermedad
from models.enfermedadModel import EnfermedadModel

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

enfermedadweb = Blueprint(
    "enfermedad_bp", __name__, template_folder="templates/enfermedad"
)


# @login_required
@enfermedadweb.route("/")
def index():
    enfermedadList = EnfermedadModel.get_enfermedads()
    return render_template("/enfermedad/index.html", enfermedads=enfermedadList)


# @login_required
@enfermedadweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        try:
            _nombre = request.form.get("txtNombre")
            enfermedad = Enfermedad(None, _nombre)
            print(enfermedad.to_JSON())
            EnfermedadModel.add_enfermedad(enfermedad)
            flash("Enfermedad Agregada successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


# @login_required
@enfermedadweb.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":        
        try:
            _nombre = request.form.get("txtNombre")
            enfermedad = Enfermedad(id, _nombre)
            EnfermedadModel.update_enfermedad(enfermedad)
            flash("Enfermedad Updated Successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


@enfermedadweb.route("/update/<id>", methods=["GET", "POST"])
def delete(id):
    enfermedad = Enfermedad(id, "Elimina")
    EnfermedadModel.delete(enfermedad)
    return redirect("/enfermedad")
