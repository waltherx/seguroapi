from flask import Flask
from flask import Blueprint
from flask import (
    render_template,
    flash
)

from models.entities.Chofer import Chofer
from models.choferModel import ChoferModel

chofersweb = Blueprint("chofer_bp", __name__, template_folder="templates/chofer")


# @login_required
@chofersweb.route("/")
def index():
    choferList = ChoferModel.get_chofers()
    return render_template("/chofer/index.html", chofers=choferList)