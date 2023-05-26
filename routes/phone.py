from flask import Blueprint, jsonify, request

# Entities
from models.entities.Phone import Phone

# Models
from models.phoneModel import PhoneModel

PhoneApi = Blueprint("phone_blueprint", __name__)


@PhoneApi.route("/<ci>")
def get_phone(ci):
    if not ci.isdigit():
        return jsonify({"message": "Ingrese solo números para CI"}), 400
    try:
        phone = PhoneModel.get_phone(ci)
        if phone != None:
            return jsonify({"telefonos": phone}), 200
        else:
            return jsonify({"message": "ingrese un Ci"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/<ci>/<id>")
def get_phone_by(ci, id):
    if not ci.isdigit() or not id.isdigit():
        return jsonify({"message": "Ingrese solo números para CI y ID"}), 400
    try:
        phone = PhoneModel.get_phone_by(ci, id)
        if phone is not None:
            return jsonify(phone), 200
        else:
            return jsonify({"message": "No se encontró el teléfono"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/add", methods=["POST"])
def add_phone():
    try:
        data = request.json
        ci_persona = data.get("ci_persona")
        numero = data.get("numero")
        referencia = data.get("referencia")

        if not ci_persona or not numero or not referencia:
            return (
                jsonify({"message": "La CI, el número y la referencia son requeridos"}),
                400,
            )

        phone = Phone(None, numero, referencia, ci_persona)
        affected_rows = PhoneModel.add_phone(phone)

        if affected_rows == 1:
            return jsonify({"message": "Teléfono agregado exitosamente"}), 200
        else:
            return jsonify({"message": "Error al insertar el teléfono"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@PhoneApi.route("/update/", methods=["PUT", "PATCH"])
def update_phone():
    try:
        if request.method not in ["PUT", "PATCH"]:
            return jsonify({"message": "Método no permitido"}), 405
        data = request.json
        print(data)
        id_telefono = data.get("id_telefono")
        numero = data.get("numero")
        referencia = data.get("referencia")
        if id_telefono is None or numero is None or referencia is None:
            return (
                jsonify(
                    {
                        "message": "Los campos id_telefono, numero y referencia son requeridos"
                    }
                ),
                400,
            )
        phone = Phone(id_telefono, numero, referencia)
        affected_rows = PhoneModel.update_phone(phone)
        if affected_rows == 1:
            return jsonify({"message": "Teléfono actualizado correctamente"}), 200
        else:
            return jsonify({"message": "No se pudo actualizar el teléfono"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

@PhoneApi.route("/delete/<id>", methods=["DELETE"])
def delete_phone(id):
    try:
        if id:
            affected_rows = PhoneModel.delete_phone(id)
            if affected_rows == 1:
                return jsonify({"message": "Teléfono eliminado exitosamente"}), 200
            else:
                return (
                    jsonify({"message": "No se encontró el teléfono para eliminar"}),
                    404,
                )
        else:
            return jsonify({"message": "El ID del teléfono es requerido"}), 400
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
