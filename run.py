from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from decouple import config
from flask_qrcode import QRcode
from flask_cors import CORS

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

# from flask_session import Session

from models.userModel import UserModel

from routes import phone
from routes import enfermedad
from routes import alergia
from routes import persona
from routes import paciente
from routes import hospital
from routes import ambulancia
from routes import chofer
from routes import user
from routes import documento
from routes import token
from routes import notificacion
from routes import paramedico
from routes import medico
from routes import emergencia
from routes import operacion
from routes import vacuna
from routes import medicamento



from models.entities.User import User

from controllers.AlergiaController import alergiaweb
from controllers.EnfermedadController import enfermedadweb
from controllers.PersonaController import personaweb
from controllers.UserController import usersweb
from controllers.ParamedicoController import paramedicoweb
from controllers.ChoferControlller import chofersweb
from controllers.MedicoController import medicosweb
from controllers.AmbulanciaController import ambulanciaweb
from controllers.DocumentoController import documentoWeb
from controllers.HospitalController import hospitalweb

from controllers.PacienteController import pacienteweb



app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")

qrcode = QRcode(app)

login_manager_app = LoginManager(app)

CORS(app, resources={"*": {"origins": "*"}})

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Usuario Salio", "success")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return render_template("/home.html")
    else:
        if request.method == "POST":
            _nameuser = request.form.get("txtNombre")
            _password = request.form.get("txtPassword")
            _user = User(None, _nameuser, _password, None, None, None, None)
            if _user:
                if _nameuser and _password:
                    user_loged = UserModel.login(_user)
                    if user_loged != None:
                        login_user(user_loged)
                        flash("bienvenido", "success")
                        return render_template("/home.html")
                    else:
                        flash("Nombre de Usuario o contrasenia no coincide")
                        return render_template("/user/login.html")
                flash("datos vacios")
                return render_template("/user/login.html")
            flash("usuario no regristrado")
            return render_template("/user/login.html")
    return render_template("/user/login.html")

@login_manager_app.user_loader
def load_user(user_id):
    user = UserModel.get_user(user_id)
    return user


@app.route("/home")
@login_required
def home():
    return render_template("/home.html")


@app.route("/")
@login_required
def home1():
    return render_template("/home.html")


def page_not_found(error):
    return render_template("404.html"), 404


def page_not_authorized(error):
    return redirect(url_for("login"))


# Blueprints App Web
app.register_blueprint(alergiaweb, url_prefix="/alergia")
app.register_blueprint(enfermedadweb, url_prefix="/enfermedad")
app.register_blueprint(personaweb, url_prefix="/persona")
app.register_blueprint(chofersweb, url_prefix="/chofer")
app.register_blueprint(paramedicoweb, url_prefix="/paramedico")
app.register_blueprint(ambulanciaweb, url_prefix="/ambulancia")
app.register_blueprint(usersweb, url_prefix="/user")
app.register_blueprint(documentoWeb, url_prefix="/documento")
app.register_blueprint(hospitalweb, url_prefix="/hospital")
app.register_blueprint(medicosweb, url_prefix="/medico")

app.register_blueprint(pacienteweb, url_prefix="/paciente")

# Blueprints Api Rest fun
app.register_blueprint(user.UserApi, url_prefix="/api/user")
app.register_blueprint(phone.PhoneApi, url_prefix="/api/phone")
app.register_blueprint(alergia.AlergiaApi, url_prefix="/api/alergia")
app.register_blueprint(enfermedad.EnfermedadApi, url_prefix="/api/enfermedad")
app.register_blueprint(hospital.HospitalApi, url_prefix="/api/hospital")
app.register_blueprint(paciente.PacienteApi, url_prefix="/api/paciente")
app.register_blueprint(ambulancia.AmbulanciaApi, url_prefix="/api/ambulancia")
app.register_blueprint(chofer.ChoferApi, url_prefix="/api/chofer")
app.register_blueprint(documento.DocumentoApi, url_prefix="/api/doc")
app.register_blueprint(token.TokenApi, url_prefix="/api/token")
app.register_blueprint(notificacion.NotificacionApi, url_prefix="/api/notificacion")
app.register_blueprint(paramedico.ParamedicoApi, url_prefix="/api/paramedico")
app.register_blueprint(medico.MedicoApi, url_prefix="/api/medico")
app.register_blueprint(emergencia.EmergenciaApi, url_prefix="/api/emergencia")
app.register_blueprint(persona.PersonaApi, url_prefix="/api/person")
app.register_blueprint(operacion.OperacionApi, url_prefix="/api/operacion")
app.register_blueprint(vacuna.VacunaApi, url_prefix="/api/vacuna")
app.register_blueprint(medicamento.MedicamentoApi, url_prefix="/api/medicamento")


# Error handlers
app.register_error_handler(401, page_not_authorized)
app.register_error_handler(404, page_not_found)
# inits

if __name__ == "__main__":
    app.run(debug=True)
