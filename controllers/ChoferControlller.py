from flask_login import login_required
from flask import Blueprint
from flask import render_template, flash

from models.entities.Chofer import Chofer
from models.choferModel import ChoferModel

chofersweb = Blueprint("chofer_bp", __name__, template_folder="templates/chofer")


@chofersweb.route("/")
@login_required
def index():
    choferList = ChoferModel.get_chofers_persons()
    return render_template("/chofer/index.html", chofers=choferList)
