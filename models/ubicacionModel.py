from database.db import get_connection
from .entities.Ubicacion import Ubicacion


class UbicacionModel:
    """@classmethod
    def get_ubicacions(self, id_dispositivo: int):
        try:
            sQuery = f""
            connection = get_connection()
            ubicacions = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    ubicacion = Ubicacion(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    ubicacions.append(ubicacion.to_JSON())
                connection.close()
            return ubicacions
        except Exception as ex:
            raise Exception(ex)"""

    @classmethod
    def view_ubicacion(self, id: int):
        try:
            sQuery = f"SELECT idubi, latitud, longitud, hora, persona_ci, dispositivo_id FROM public.ubicacion where idubi={id};"
            connection = get_connection()
            ubicacion = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row:
                    ubicacion = Ubicacion(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    ubicacion = ubicacion.to_JSON()
                connection.close()
            return ubicacion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_ubicacion(self, ubicacion: Ubicacion):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.ubicacion (latitud, longitud, hora, persona_ci, dispositivo_id) VALUES({ubicacion.latitud}, {ubicacion.longitud}, now() AT TIME ZONE 'America/La_Paz', {ubicacion.persona_ci}, {ubicacion.dispositivo_id});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_ubicacion(self, id: int):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.ubicacion WHERE idubi = {id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def last_ubicacion(self,ci :int):
        try:
            sQuery = f"SELECT idubi, latitud, longitud, hora, persona_ci, dispositivo_id FROM public.ubicacion where persona_ci = {ci} ORDER BY idubi desc LIMIT 1;"
            connection = get_connection()
            ubicacion = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row:
                    ubicacion = Ubicacion(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    ubicacion = ubicacion.to_JSON()
                connection.close()
            return ubicacion
        except Exception as ex:
            raise Exception(ex)
