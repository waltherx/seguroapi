from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from decouple import config
from flask_cors import CORS
 
from route import phone
from route import enfermedad
from route import alergia
from route import persona
from route import hospital
from route import siniestro

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY']=config('SECRET_KEY')

#CORS(app, resources={"*": {"origins": "http://localhost:9300"}})

@app.route('/v')
def home():
    return render_template('home.html')

@app.route('/p')
def pac():
    return render_template('persona/index.html')

@app.route('/')
def index():
    return render_template('login.html')

def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404

# Blueprints
app.register_blueprint(phone.PhoneApi, url_prefix="/api/phone")
app.register_blueprint(alergia.AlergiaApi, url_prefix="/api/alergia")
app.register_blueprint(enfermedad.EnfermedadApi, url_prefix="/api/enfermedad")    
app.register_blueprint(hospital.HospitalApi, url_prefix="/api/hospital")
app.register_blueprint(siniestro.SiniestroApi, url_prefix="/api/siniestro")
app.register_blueprint(persona.PersonaApi, url_prefix="/api/persona")
# Error handlers
app.register_error_handler(404, page_not_found)
# inits
csrf.init_app(app)
if __name__ == "__main__":
    app.run()