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
        # if _user.id != None:
        ok = UserModel.update_user(_user)
        return jsonify({"message": "usuario actualisado"}), 200
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/token", methods=["PUT"])
def update_user_token():
    try:
        _id = request.json["id"]
        _token = request.json["token"]
        _user = User(_id, None, None, None, None, _token, None)
        # if _user.id != None:
        ok = UserModel.update_user_token(_user)
        return jsonify({"message": "usuario token actualisado"}), 200
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
