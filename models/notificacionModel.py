from database.db import get_connection
from .entities.Notificacion import Notificacion


class NotificacionModel:
    @classmethod
    def add_notif(self, notif):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.notificacion (titulo, descripcion, fecha_creacion, fecha_envio, user_destino, user_remitente, leido) VALUES('{notif.titulo}', '{notif.descripcion}', NOW(), null, {notif.user_destino}, {notif.user_remitente}, false);"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_notifs(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idnoti, titulo, descripcion, fecha_creacion, fecha_envio, user_destino, user_remitente, leido FROM public.notificacion where user_remitente = {id} and leido = false;"
            notifs = []
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                resultset = cursor.fetchall()
                for row in resultset:
                    noti = Notificacion(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    notifs.append(noti.to_JSON())
            connection.close()
            return notifs
        except Exception as ex:
            raise Exception(ex)
