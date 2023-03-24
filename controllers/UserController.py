from flask import Flask
from flask import Blueprint
from flask import (
    config,
    render_template,
    redirect,
    url_for,
    request,
    abort,
    flash,
)
from models.entities.User import User
from models.userModel import UserModel

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

enfermedadweb = Blueprint(
    "enfermedad_bp", __name__, template_folder="templates/enfermedad"
)


# @login_required
@enfermedadweb.route("/")
def index():
    userList = UserModel.get_users()
    return render_template("/user/index.html", users=userList)


# @login_required
@enfermedadweb.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        try:
            _name = request.form.get("txtNombre")
            _password = request.form.get("txtPassword")
            _email = request.form.get("txtEmail")
            # _rol = request.form.get("txtRol")
            user = User(None, _name, _password, _email, None, 1)
            UserModel.add_user(user)
            flash("User Agregada successfully")
            return redirect("/user")
        except Exception as e:
            flash(e.args[1])
            return redirect("/user")


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
