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
from models.entities.Alergia import Alergia
from models.alergiaModel import AlergiaModel

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

alergiaweb = Blueprint(
    "alergia_bp", __name__, template_folder="templates/alergia"
)


# @login_required
@alergiaweb.route("/")
def index():
    alergiaList = AlergiaModel.get_alergias()
    return render_template("/alergia/index.html", alergias=alergiaList)


# @login_required
@alergiaweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        _nombre = request.form["txtNombre"]
        try:
            alergia = Alergia(None, _nombre)
            AlergiaModel.add_alergia(alergia)
            flash("Alergia Agregada successfully")
            return redirect("/alergia")
        except Exception as e:
            flash(e.args[1])
            return redirect("/alergia")


# @login_required
@alergiaweb.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        _nombre = request.form.get("nombre")
        try:
            alergia = Alergia(id, _nombre)
            AlergiaModel.update_alergia(alergia)
            flash("Alergia Updated Successfully")
            return redirect("/alergia")
        except Exception as e:
            flash(e.args[1])
            return redirect("/alergia")


@alergiaweb.route("/update/<id>", methods=["GET", "POST"])
def delete(id):
    alergia = Alergia(id, "Elimina")
    AlergiaModel.delete_alergia(alergia)
    return redirect("/alergia")
