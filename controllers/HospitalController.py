from flask import Flask
from flask import Blueprint
from flask import (
    render_template,
    flash
)

from models.entities.Hospital import Hospital
from models.hospitalModel import HospitalModel

hospitalweb = Blueprint("chofer_bp", __name__, template_folder="templates/hospital")


# @login_required
@hospitalweb.route("/")
def index():
    hList = HospitalModel.get_hospitals()
    return render_template("/hospital/index.html", hospitals=hList)