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
from models.entities.Vacuna import Vacuna
from models.vacunaModel import VacunaModel

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

vacunaweb = Blueprint("vacuna_bp", __name__, template_folder="templates/vacuna")


# @login_required
@vacunaweb.route("/create/<ci>", methods=["POST"])
def create(ci):
    if request.method == "POST":
        _nombre = request.form["txtNombre"]
        _dosis = request.form["txtDosis"]
        try:
            vacuna = Vacuna(None, _nombre, _dosis, ci)
            VacunaModel.add_alergia(vacuna)
            flash("Vacuna Agregada successfully")
            return redirect("/paciente/view/"+str(ci))
        except Exception as e:
            flash(e.args[1])
            return redirect("/paciente")
