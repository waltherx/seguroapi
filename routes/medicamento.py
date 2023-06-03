from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

# Entities
from models.entities.Medicamento import Medicamento

# Models
from models.medicamentoModel import MedicamentoModel

MedicamentoApi = Blueprint("medicamento_blueprint", __name__)


@MedicamentoApi.route("/<ci>", methods=["GET"])
def get_medicamento(ci):
    try:
        medicamento = MedicamentoModel.get_medicamento(ci)
        if medicamento != None:
            return jsonify(medicamento), 200
        else:
            return jsonify({"msg": "az"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


def validate_medicamento_data(data, is_update: bool):
    print(data, is_update)
    if is_update:
        required_fields = ["id", "nombre"]
    else:
        required_fields = ["id_paciente", "nombre"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        raise BadRequest(
            f"Los campos obligatorios {', '.join(missing_fields)} están ausentes"
        )
        
    id = data.get("id", 0)
    id_paciente = data.get("id_paciente", 0)
    nombre = data["nombre"]
    descripcion = data.get("descripcion", "")
    cantidad = data.get("cantidad")
    unidad = data.get("unidad", "")
    
    if cantidad is not None and not isinstance(cantidad, int):
        print("La cantidad no es un número entero.")
        cantidad = 0
    return Medicamento(id, nombre, descripcion, cantidad, unidad, id_paciente)


@MedicamentoApi.route("/add", methods=["POST"])
def add_medicamento():
    if request.method != "POST":
        return jsonify({"message": "La solicitud debe ser de tipo POST"}), 405
    try:
        data = request.get_json()
        medicamento = validate_medicamento_data(data, False)
        affected_rows = MedicamentoModel.add_medicamento(medicamento)

        if affected_rows == 1:
            return jsonify({"message": "Medicamento Agregada!"}), 201
        else:
            return jsonify({"message": "Error al insertar Medicamento"}), 500

    except BadRequest as e:
        return jsonify({"message": str(e)}), 400

    except Exception as e:
        return jsonify({"message": "Error interno del servidor"}), 500


@MedicamentoApi.route("/view/<id>", methods=["GET"])
def view_medicam(id):
    try:
        if request.method == "GET":
            medicam = MedicamentoModel.view_medicamentos(id)
            if medicam is not None:
                return jsonify(medicam), 200
            else:
                return jsonify({"message": "no se encontro Medicamento!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/update", methods=["PUT"])
def update_medicamento():
    try:
        if request.method == "PUT" or request.method == "PATCH":
            data = request.get_json()
            medicamento = validate_medicamento_data(data, True)
            print(medicamento.to_JSON())
            if MedicamentoModel.update_medicamento(medicamento):
                return jsonify({"message": "Medicamento Actualizada!"}), 200
            else:
                return jsonify({"message": "Medicamento no Actualizada!"}), 404
        else:
            return jsonify({"message": "Metodo no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@MedicamentoApi.route("/delete/<id>", methods=["DELETE"])
def delete_medicamento(id):
    try:
        if request.method == "DELETE":
            affected_rows = MedicamentoModel.delete_medicamento(id)
            if affected_rows == 1:
                return jsonify({"message": "Medicamento Eliminado!"}), 200
            else:
                return jsonify({"message": "Medicamento no Eliminado!"}), 404
        return jsonify({"message": "Metodo no valido!"}), 405
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
