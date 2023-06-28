from flask import Blueprint, jsonify, request

# Entities
from models.entities.User import User

# Models
from models.userModel import UserModel

from werkzeug.security import generate_password_hash, check_password_hash

UserApi = Blueprint("user_blueprint", __name__)


@UserApi.route("/")
def get_users():
    try:
        users = UserModel.get_users()
        return jsonify(users), 200
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/view/<id>", methods=["GET"])
def view_user(id):
    try:
        _user = UserModel.get_user_id(id)
        if _user:
            return jsonify({"data": _user}), 200
        else:
            return jsonify({"message1": "Usuario no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message1": str(ex)}), 500


@UserApi.route("/<id>", methods=["GET"])
def get_user(id):
    try:
        _user = UserModel.get_user_id(id)
        if _user:
            return jsonify({"data": _user}), 200
        else:
            return jsonify({"message1": "Usuario no encontrado"}), 404
    except Exception as ex:
        return jsonify({"message1": str(ex)}), 500


@UserApi.route("/add", methods=["POST"])
def add_user():
    try:
        _ci = request.json["ci_persona"]
        _nameuser = request.json["nameuser"]
        _password = request.json["password"]
        _email = request.json["email"]
        _idrol = request.json["id_rol"]
        _user = User(None, _nameuser, _password, _email, None, None, _idrol, _ci)
        UserModel.add_user(_user)
        return jsonify({"message": "usuario agregado"}), 200
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/passwprd", methods=["PUT"])
def change_password():
    try:
        data = request.get_json()
        id = data["id"]
        pwd = data["password"]
        pwd2 = data["password2"]

        pwd_lower = pwd.lower()
        pwd2_lower = pwd2.lower()

        if len(pwd_lower) == len(pwd2_lower) and pwd_lower == pwd2_lower:
            affected_rows = UserModel.change_password(id, pwd, pwd2)
            if affected_rows:
                return {"message": "Contraseña cambiada correctamente."}
            else:
                return {"message": "Contraseña no cambiada!"}
        else:
            return {"message": "Las contraseñas no son iguales."}

    except Exception as ex:
        return None


@UserApi.route("/update", methods=["PUT"])
def update_user():
    try:
        _id = request.json["id"]
        _nameuser = request.json["nameuser"]
        _password = request.json["password"]
        _email = request.json["email"]
        _estado = request.json["estado"]
        _token = request.json["token"]
        _idrol = request.json["idrol"]
        _user = User(_id, _nameuser, _password, _email, _estado, _token, _idrol)
        affected_rows = UserModel.update_user(_user)
        if affected_rows:
            return jsonify({"message": "Usuario actualisado"}), 200
        else:
            return jsonify({"message": "Usuario no actualisado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/token", methods=["PUT"])
def update_user_token():
    try:
        _id = request.json["id"]
        _token = request.json["token"]
        _user = User(_id, None, None, None, None, _token, None)
        # if _user.id != None:
        affected_rows = UserModel.update_user_token(_user)
        if affected_rows:
            return jsonify({"message": "usuario token actualisado"}), 200
        else:
            return jsonify({"message": "usuario token no fue actualisado"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/login", methods=["POST"])
def login():
    try:
        _nameuser = request.json["nameuser"]
        _password = request.json["password"]
        _user = UserModel.get_userbyname(_nameuser)
        if _user:
            if _nameuser and _password:
                if check_password_hash(_user["password"], _password):
                    return jsonify(_user)
                else:
                    return jsonify(
                        {"message": "Nombre de Usuario o contrasenia no coincide"}
                    )
            return jsonify({"message": "datos vacios"})
        return jsonify({"message": "usuario no regristrado"})
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/p/<ci>", methods=["GET"])
def get_user_x_ci(ci):
    try:
        _user = UserModel.get_user_by_ci(ci)
        return jsonify({"data": _user}), 200
    except Exception as ex:
        return jsonify({"message1": str(ex)}), 500
