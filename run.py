from flask import Flask, render_template, request, redirect, url_for, flash
from decouple import config
from flask_login import LoginManager
from flask_qrcode import QRcode
from flask_cors import CORS

# from flask_session import Session

from routes import phone
from routes import enfermedad
from routes import alergia
from routes import persona
from routes import hospital
from routes import siniestro
from routes import ambulancia
from routes import chofer
from routes import user

from controllers.AlergiaController import alergiaweb
from controllers.EnfermedadController import enfermedadweb
from controllers.PersonaController import personaweb
from controllers.UserController import usersweb

# CORS(app, resources={"*": {"origins": "http://localhost:9300"}})
app = Flask(__name__)
app.config["SECRET_KEY"] = config("SECRET_KEY")

qrcode = QRcode(app)

#login_manager = LoginManager()
#login_manager.init_app(app)

# lasession = Session(app)
# lasession.init_app(app)

@app.route("/")
def index():
    return render_template("/user/login.html")

@app.route("/home")
def home():
    return render_template("/home.html")

def page_not_found(error):
    return render_template("404.html"), 404

# Blueprints App Web
app.register_blueprint(alergiaweb, url_prefix="/alergia")
app.register_blueprint(enfermedadweb, url_prefix="/enfermedad")
app.register_blueprint(personaweb, url_prefix="/paciente")
app.register_blueprint(usersweb, url_prefix="/user")

# Blueprints Api Rest
app.register_blueprint(user.UserApi, url_prefix="/api/user")
app.register_blueprint(phone.PhoneApi, url_prefix="/api/phone")
app.register_blueprint(alergia.AlergiaApi, url_prefix="/api/alergia")
app.register_blueprint(enfermedad.EnfermedadApi, url_prefix="/api/enfermedad")
app.register_blueprint(hospital.HospitalApi, url_prefix="/api/hospital")
app.register_blueprint(siniestro.SiniestroApi, url_prefix="/api/siniestro")
app.register_blueprint(persona.PersonaApi, url_prefix="/api/paciente")
app.register_blueprint(ambulancia.AmbulanciaApi, url_prefix="/api/ambulancia")
app.register_blueprint(chofer.ChoferApi, url_prefix="/api/chofer")
# Error handlers
app.register_error_handler(404, page_not_found)
# inits

if __name__ == "__main__":
    app.run(debug=True)
