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
    jsonify,
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
        _nombre = request.form["txtNombre"]
        try:
            enfermedad = Enfermedad(None, _nombre)
            print(enfermedad.to_JSON())
            EnfermedadModel.add_enfermedad(enfermedad)
            flash("Enfermedad Agregada successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


# @login_required
@enfermedadweb.route("/update/<id>", methods=["PUT"])
def update():
    if request.method == "PUT":
        _idenf = request.form["idenf"]
        _nombre = request.form["nombre"]
        enfermedad = Enfermedad(_idenf, _nombre)
        EnfermedadModel.update_enfermedad(enfermedad)
        flash("Enfermedad Updated Successfully")
        return redirect("/enfermedad")

"""
def delete(enfermedad_id):
    enfermedad = Enfermedad(enfermedad_id, "Elimina")
    EnfermedadModel.delete(enfermedad)
    return redirect("/enfermedad")
"""
