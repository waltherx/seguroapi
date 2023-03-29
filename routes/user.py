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
        return jsonify(users)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@UserApi.route("/<id>")
def get_user(id):
    try:
        _user = UserModel.get_user(id)
        return jsonify(_user)
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
