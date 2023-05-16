from flask_login import login_required
from flask import Blueprint,request
from flask import render_template, flash

from models.medicoModel import MedicoModel

medicosweb = Blueprint("medico_bp", __name__, template_folder="templates/chofer")


@medicosweb.route("/")
@login_required
def index():
    medicoList = MedicoModel.get_medicos_persons()
    return render_template("/medico/index.html", medicos=medicoList)
