from flask_login import login_required
from flask import Blueprint
from flask import render_template, flash
from decouple import config

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
    print(_paciente)
    return render_template("/paciente/view.html", paciente=_paciente)

@pacienteweb.route("/ubicacion", methods=["GET", "POST"])
@login_required
def ubicaion():    
    _ia = config("MAPBOX_KEY")
    mapbox_url = "mapbox://styles/carlps/cj6qydf6v3xju2rpqsre0immg"
    return render_template(
        "/paciente/map.html", ACCESS_KEY=_ia, mapbox_url=mapbox_url
    )


