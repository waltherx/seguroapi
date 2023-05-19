from flask_login import login_required
from flask import Blueprint
from flask import render_template, flash
from decouple import config

from models.entities.Hospital import Hospital
from models.hospitalModel import HospitalModel

hospitalweb = Blueprint("hospital_bp", __name__, template_folder="templates/hospital")


@hospitalweb.route("/")
@login_required
def index():
    _ia = config("MAPBOX_KEY")
    mapbox_url = "mapbox://styles/carlps/cj6qydf6v3xju2rpqsre0immg"
    hList = HospitalModel.get_hospitals()
    return render_template(
        "/hospital/index.html", hospitals=hList, ACCESS_KEY=_ia, mapbox_url=mapbox_url
    )
