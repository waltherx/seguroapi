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
            enfermedads = []
            connection = get_connection()
            sQuery= f"SELECT e.idenf, e.nombre, e.descripcion, e.causa, e.sintoma, e.diagnostico, e.paciente_id FROM enfermedad e, persona p ,paciente w where e.paciente_id = w.idpac and p.ci =w.ci_persona and p.ci = { id } ;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                enfermedad = None
                for row in resultset:
                    enfermedad = Enfermedad(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    enfermedads.append(enfermedad.to_JSON())
            connection.close()
            return enfermedads
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
