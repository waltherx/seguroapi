from flask_login import login_required
from flask import Blueprint
from flask import (
    render_template,
    redirect,
    request,
    flash,
)

from models.entities.User import User
from models.userModel import UserModel
from werkzeug.security import generate_password_hash

usersweb = Blueprint("user_bp", __name__, template_folder="templates/user")


@usersweb.route("/")
@login_required
def index():
    userList = UserModel.get_users()
    return render_template("/user/index.html", users=userList)


@usersweb.route("/create", methods=["POST"])
@login_required
def create():
    if request.method == "POST":
        try:
            _name = request.form.get("txtNombre")
            _pass = request.form.get("txtPassword")
            _password = generate_password_hash(_pass)
            _email = request.form.get("txtEmail")
            _rol = request.form.get("txtRol")
            User
            user = User(None, _name, _password, _email, None, _rol)
            UserModel.add_user(user)
            flash("User Agregada successfully")
            return redirect("/user")
        except Exception as e:
            flash(e.args[1])
            return redirect("/user")


@usersweb.route("/view", methods=["GET"])
@login_required
def view():
    return render_template("user/view.html")


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
