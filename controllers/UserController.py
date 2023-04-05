from flask import Flask
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

from werkzeug.security import check_password_hash

# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

usersweb = Blueprint("user_bp", __name__, template_folder="templates/user")


# @login_required
@usersweb.route("/")
def index():
    userList = UserModel.get_users()
    return render_template("/user/index.html", users=userList)


# @login_required
@usersweb.route("/create", methods=["POST"])
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


@usersweb.route("/login", methods=["POST"])
def login():
    _nameuser = request.form.get("txtNombre")
    _password = request.form.get("txtPassword")
    _user = UserModel.get_userbyname(_nameuser)
    if _user:
        if _nameuser and _password:
            if check_password_hash(_user["password"], _password):
                flash("bienvenido")
                return render_template("/home.html",user_nombre=_nameuser)
            else:
                flash("Nombre de Usuario o contrasenia no coincide")
                return render_template("/user/login.html")
        flash("datos vacios")
        return render_template("/user/login.html")
    flash("usuario no regristrado")
    return render_template("/user/login.html")


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
