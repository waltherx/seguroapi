from decouple import config
from flask import Flask, redirect, render_template, request, url_for
from flask_cors import CORS
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from controllers.AmbulanciaController import ambulanciaweb
from controllers.ChoferControlller import chofersweb
from controllers.DocumentoController import documentoWeb
from controllers.HospitalController import hospitalweb
from controllers.MedicoController import medicosweb
from controllers.PacienteController import pacienteweb
from controllers.ParamedicoController import paramedicoweb
from controllers.PersonaController import personaweb
from controllers.UserController import usersweb
from models.emergenciaModel import EmergenciaModel
from models.entities.Emergencia import Emergencia
from models.entities.User import User
from models.userModel import UserModel
from routes import (
    alergia,
    ambulancia,
    chofer,
    dispositivo,
    documento,
    emergencia,
    enfermedad,
    hospital,
    medicamento,
    medico,
    notificacion,
    operacion,
    paciente,
    paramedico,
    persona,
    phone,
    token,
    ubicacion,
    user,
    vacuna,
)

# from flask_session import Session


app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")

login_manager_app = LoginManager(app)

CORS(app, resources={"*": {"origins": "*"}})


@app.route("/logout")
@login_required
def logout():
    logout_user()
    #   flash("Usuario Salio", "success")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    Error = None
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
                        # flash("bienvenido", "success")
                        return redirect(url_for("home1"))
                    else:
                        Error = "Nombre de Usuario o contrasenia no coincide"
                        return render_template("/user/login.html", error=Error)
                Error = "Ingrese datos por favor"
                return render_template("/user/login.html", error=Error)
            Error = "usuario no regristrado"
            return render_template("/user/login.html", error=Error)
    return render_template("/user/login.html", error=Error)


@login_manager_app.user_loader
def load_user(user_id):
    user = UserModel.view_user(user_id)
    return user


@app.route("/home")
@login_required
def home():
    return render_template("/home.html")


@app.route("/")
@login_required
def home1():
    return render_template("/home.html")


"""
@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403
"""


@app.errorhandler(410)
def page_gone(e):
    return render_template("410.html"), 410


def page_not_found(error):
    return render_template("404.html"), 404


def page_not_authorized(error):
    return redirect(url_for("login"))


# Blueprints App Web
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
app.register_blueprint(dispositivo.DispositivoApi, url_prefix="/api/dispo")
app.register_blueprint(ubicacion.UbicacionApi, url_prefix="/api/ubicacion")


# Error handlers
app.register_error_handler(401, page_not_authorized)
app.register_error_handler(404, page_not_found)
# inits

if __name__ == "__main__":
    app.run(port=5000, debug=True)
