from flask import Flask
from flask import Blueprint
from flask import (
    render_template,
    flash
)

from models.entities.Paramedico import Paramedico
from models.paramedicoModel import ParamedicoModel

paramedicoweb = Blueprint("paramedico_bp", __name__, template_folder="templates/paramedico")


# @login_required
@paramedicoweb.route("/")
def index():
    pList = ParamedicoModel.get_paramedicosA()
    return render_template("/paramedico/index.html", paramedicos=pList)