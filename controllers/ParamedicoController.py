from flask_login import login_required
from flask import Blueprint
from flask import (
    render_template,
    flash
)

from models.entities.Paramedico import Paramedico
from models.paramedicoModel import ParamedicoModel

paramedicoweb = Blueprint("paramedico_bp", __name__, template_folder="templates/paramedico")

@paramedicoweb.route("/")
@login_required
def index():
    pList = ParamedicoModel.get_paramedicosA()
    return render_template("/paramedico/index.html", paramedicos=pList)