from database.db import get_connection
from .entities.Siniestro import Siniestro


class SiniestrolModel:
    @classmethod
    def get_siniestros(self):
        try:
            connection = get_connection()
            siniestros = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT ids, descripcion, to_char(fecha,'DD-MM-YYYY HH:MM:SS'), lat, longi, idper FROM siniestro")
                resultset = cursor.fetchall()
                for row in resultset:
                    siniestro = Siniestro(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    siniestros.append(siniestro.to_JSON())

            connection.close()
            return siniestros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_siniestro(self, id):
        try:
            connection = get_connection()
            siniestros = []

            with connection.cursor() as cursor:
                sQuery = f"SELECT ids, descripcion, to_char(fecha,'DD-MM-YYYY HH:MM:SS'), lat, longi, idper FROM siniestro WHERE idper = { id }"
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    siniestro = Siniestro(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    siniestros.append(siniestro.to_JSON())
                row = cursor.fetchone()

            connection.close()
            return siniestros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_siniestro(self, siniestro):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO siniestro (descripcion, fecha, lat, longi, idper) VALUES ('{siniestro.descripccion}','{siniestro.fecha}',{siniestro.lat},{siniestro.long},{siniestro.idper})"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_siniestro(self, siniestro):
        try:
            connection = get_connection()
            sQuery = f"UPDATE siniestro SET descripcion='{siniestro.descripccion}', fecha='{siniestro.fecha}', lat={siniestro.lat}, longi={siniestro.long} WHERE ids = {siniestro.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_siniestro(self, siniestro):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM siniestro WHERE ids = {siniestro.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
