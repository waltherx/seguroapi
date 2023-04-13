from flask_login import login_required
from flask import Blueprint
from flask import (
    render_template,
    flash
)
from decouple import config
from models.entities.Ambulancia import Ambulancia
from models.ambulanciaModel import AmbulanciaModel

ambulanciaweb = Blueprint("ambulancia_bp", __name__, template_folder="templates/ambulancia")

@ambulanciaweb.route("/")
@login_required
def index():
    _ia=config('MAPBOX_KEY')
    mapbox_url = 'mapbox://styles/carlps/cj6qydf6v3xju2rpqsre0immg'
    aList = AmbulanciaModel.get_ambulancia()
    return render_template("/ambulancia/index.html", ambulancias=aList,ACCESS_KEY=_ia,mapbox_url=mapbox_url)