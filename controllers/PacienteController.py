from flask_login import login_required
from flask import Blueprint
from flask import (
    render_template,
    flash
)

from models.entities.Persona import Persona
from models.entities.Paciente import Paciente
from models.pacienteModel import PacienteModel

pacienteweb = Blueprint("paciente_bp", __name__, template_folder="templates/paciente")

@pacienteweb.route("/")
def main():
    pList = PacienteModel.get_pacs()
    return render_template("/paciente/index.html", pacients=pList)