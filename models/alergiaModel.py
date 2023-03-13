from database.db import get_connection
from .entities.Alergia import Alergia


class AlergiaModel:
    @classmethod
    def get_alergias(self):
        try:
            connection = get_connection()
            alergias = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT idale, nombre FROM alergia ORDER BY idale ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    alergia = Alergia(row[0], row[1])
                    alergias.append(alergia.to_JSON())

            connection.close()
            return alergias
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_alergia(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idale, nombre FROM alergia WHERE idale = %s", (id,)
                )
                row = cursor.fetchone()

                alergia = None
                if row != None:
                    alergia = Alergia(row[0], row[1])
                    alergia = alergia.to_JSON()

            connection.close()
            return alergia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_alergia(self, alergia):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO alergia (nombre) VALUES ('{alergia.nombre}')"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_alergia(self, alergia):
        try:
            connection = get_connection()
            sQuery = f"UPDATE alergia SET nombre = '{alergia.nombre}' WHERE idenf = {alergia.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_alergia(self, alergia):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM alergia WHERE idenf = {alergia.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
