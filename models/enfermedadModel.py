from database.db import get_connection
from .entities.Enfermedad import Enfermedad

class EnfermedadModel:
    @classmethod
    def get_enfermedads(self):
        try:
            connection = get_connection()
            enfemedads = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idenf, nombre FROM enfermedad ORDER BY idenf ASC"
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    enfermedad = Enfermedad(row[0], row[1])
                    enfemedads.append(enfermedad.to_JSON())
            connection.close()
            return enfemedads
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_enfermedad(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idenf, nombre FROM enfermedad WHERE idenf = %s", (id,)
                )
                row = cursor.fetchone()
                enfermedad = None
                if row != None:
                    enfermedad = Enfermedad(row[0], row[1])
                    enfermedad = enfermedad.to_JSON()
            connection.close()
            return enfermedad
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_enfermedad(self, enfermedad):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO enfermedad (nombre) VALUES ('{enfermedad.nombre}')"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_enfermedad(self, enfermedad):
        try:
            connection = get_connection()
            sQuery = f"UPDATE enfermedad SET nombre = '{enfermedad.nombre}' WHERE idenf = {enfermedad.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_enfermedad(self, enfermedad):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM enfermedad WHERE idenf = {enfermedad.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
