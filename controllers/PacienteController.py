from flask_login import login_required
from flask import Blueprint
from flask import render_template, flash

from models.pacienteModel import PacienteModel

pacienteweb = Blueprint("paciente_bp", __name__, template_folder="templates/paciente")


@pacienteweb.route("/")
@login_required
def main():
    pList = PacienteModel.get_pacs()
    return render_template("/paciente/index.html", pacients=pList)


@pacienteweb.route("/<ci>", methods=["GET", "POST"])
@login_required
def view(ci:int):
    _paciente = PacienteModel.get_paciente_X_ci(ci)
    return render_template("/paciente/view.html", paciente=_paciente)
