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
    def get_enfermedad(self, ci):
        try:
            enfermedads = []
            connection = get_connection()
            sQuery = f"SELECT e.idenf, e.nombre, e.descripcion, e.causa, e.sintoma, e.diagnostico, e.paciente_id FROM enfermedad e, persona p ,paciente w where e.paciente_id = w.idpac and p.ci =w.ci_persona and p.ci = {ci} order by e.idenf asc;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                enfermedad = None
                for row in resultset:
                    enfermedad = Enfermedad(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                    )
                    enfermedads.append(enfermedad.to_JSON())
            connection.close()
            return enfermedads
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_enfermedad(self, id):
        try:
            connection = get_connection()
            sQuery = f"SELECT idenf, nombre, descripcion, causa, sintoma, diagnostico, paciente_id FROM public.enfermedad where idenf = {id} ;"
            enfermedad = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row != None:
                    enfermedad = Enfermedad(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                    )
                    enfermedad = enfermedad.to_JSON()
                connection.close()
            return enfermedad
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_enfermedad(self, enfermedad):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.enfermedad (nombre, descripcion, causa, sintoma, diagnostico, paciente_id) VALUES('{enfermedad.nombre}', '{enfermedad.descripcion}', '{enfermedad.causa}', '{enfermedad.sintoma}', '{enfermedad.diagnostico}', {enfermedad.paciente_id});"
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
            sQuery = f"UPDATE public.enfermedad SET nombre='{enfermedad.nombre}', descripcion='{enfermedad.descripcion}', causa='{enfermedad.causa}', sintoma='{enfermedad.sintoma}', diagnostico='{enfermedad.diagnostico}' WHERE idenf={enfermedad.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_enfermedad(self, id):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.enfermedad WHERE idenf={id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
