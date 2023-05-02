from flask import Blueprint, jsonify, request

# Entities
from models.entities.Notificacion import Notificacion

# Models
from models.notificacionModel import NotificacionModel

NotificacionApi = Blueprint("notificacion_blueprint", __name__)


@NotificacionApi.route("/<id>")
def get_notifs(id):
    try:
        notifs = NotificacionModel.get_notifs(id)
        if notifs != None:
            return jsonify({"Notificaciones": notifs}), 200
        else:
            return (
                jsonify({"message": "nose encontro notificaciones con este id :" + id}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@NotificacionApi.route("/des/<id>")
def get_notifdes(id):
    try:
        notifs = NotificacionModel.get_notifdes(id)
        if notifs != None:
            return jsonify({"Notificaciones": notifs}), 200
        else:
            return (
                jsonify({"message": "nose encontro notificaciones con este id :" + id}),
                404,
            )
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@NotificacionApi.route("/add", methods=["POST"])
def add_token():
    try:
        _id = None
        _titulo = request.json["titulo"]
        _descrip = request.json["descripcion"]
        _user_dest = request.json["user_destino"]
        _user_remi = request.json["user_remitente"]
        noti = Notificacion(
            _id, _titulo, _descrip, None, None, _user_dest, _user_remi, None
        )
        res_noti = NotificacionModel.add_notif(noti)
        if res_noti != None:
            return (
                jsonify({"id_token": res_noti, "message": "notificacion insertada!"}),
                201,
            )
        else:
            return jsonify({"message": "Error on insert"})
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500


@NotificacionApi.route("/update/r/<id>", methods=["PUT", "PATCH"])
def update_notificacion_leida(id):
    try:
        if request.method == "PATCH" or request.method == "PUT":
            if id:
                res_noti = NotificacionModel.update_read_notif(id)
                if res_noti != None:
                    return (
                        jsonify(
                            {
                                "id_notificacion": id,
                                "message": "notificacion leida actualizada!",
                            }
                        ),
                        201,
                    )
                else:
                    return jsonify({"message": "Error on update"}), 404
            else:
                return jsonify({"message": "Error on update id no valido"}), 404
        else:
            return jsonify({"message": "Error on update method no valido"}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
