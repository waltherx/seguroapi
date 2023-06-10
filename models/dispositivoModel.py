from database.db import get_connection
from .entities.Dispositivo import Dispositivo


class DispositivoModel:
    """@classmethod
    def get_dispositivos(self, id_dispositivo: int):
        try:
            sQuery = f""
            connection = get_connection()
            dispositivos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    dispositivo = dispositivo(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    dispositivos.append(dispositivo.to_JSON())
                connection.close()
            return dispositivos
        except Exception as ex:
            raise Exception(ex)"""

    @classmethod
    def view_dispositivo(self, id: int):
        try:
            sQuery = f"SELECT iddis, nombre FROM public.dispositivo where iddis={id};"
            connection = get_connection()
            dispositivo = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row:
                    dispositivo = Dispositivo(row[0], row[1])
                    dispositivo = dispositivo.to_JSON()
                connection.close()
            return dispositivo
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_dispositivo(self, dispositivo: Dispositivo):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.dispositivo (nombre) VALUES('{dispositivo.nombre}');"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_dispositivo(self, id: int):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.dispositivo WHERE iddis= {id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
