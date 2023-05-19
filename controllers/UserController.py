from datetime import datetime
from flask_login import login_required, current_user
from flask import Blueprint
from flask import (
    render_template,
    redirect,
    request,
    flash,
)

from models.entities.User import User
from models.personaModel import PersonaModel
from models.userModel import UserModel
from werkzeug.security import generate_password_hash

usersweb = Blueprint("user_bp", __name__, template_folder="templates/user")

def Calcular_edad(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

@usersweb.route("/")
@login_required
def index():
    userList = UserModel.get_users()
    return render_template("/user/index.html", users=userList)

@usersweb.route("/password")
@login_required
def password():
    return render_template("/user/password.html")

@usersweb.route("/view", methods=["GET"])
@login_required
def view():
    _persona = PersonaModel.get_persona(current_user.ci_persona)
    _birth_date = datetime.strptime(_persona["fechaNac"], "%d-%m-%Y")
    _edad = Calcular_edad(_birth_date)
    return render_template("user/view.html", persona=_persona, edad_user=_edad)


"""
# @login_required
@enfermedadweb.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        try:
            _nombre = request.form.get("txtNombre")
            enfermedad = Enfermedad(id, _nombre)
            EnfermedadModel.update_enfermedad(enfermedad)
            flash("Enfermedad Updated Successfully")
            return redirect("/enfermedad")
        except Exception as e:
            flash(e.args[1])
            return redirect("/enfermedad")


@enfermedadweb.route("/update/<id>", methods=["GET", "POST"])
def delete(id):
    enfermedad = Enfermedad(id, "Elimina")
    EnfermedadModel.delete(enfermedad)
    return redirect("/enfermedad")
"""
