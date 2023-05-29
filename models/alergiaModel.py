from database.db import get_connection
from .entities.Alergia import Alergia


class AlergiaModel:
    @classmethod
    def get_alergias(self):
        try:
            connection = get_connection()
            alergias = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idale, nombre, descripcion, gravedad, reaccion, paciente_id FROM public.alergia ORDER BY idale ASC"
                )
                resultset = cursor.fetchall()
                for row in resultset:
                    alergia = Alergia(row[0], row[1], row[2], row[3], row[4], row[5])
                    alergias.append(alergia.to_JSON())
            connection.close()
            return alergias
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_alergia(self, ci):
        try:
            connection = get_connection()
            alergias = []
            sQuery = f"SELECT l.idale, l.nombre, l.descripcion, l.gravedad, l.reaccion, l.paciente_id FROM alergia l, paciente a , persona p where p.ci =a.ci_persona and l.paciente_id =a.idpac and p.ci = {ci}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                alergia = None
                for row in resultset:
                    alergia = Alergia(row[0], row[1], row[2], row[3], row[4], row[5])
                    alergias.append(alergia.to_JSON())
            connection.close()
            return alergias
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_alergia(self, id):
        try:
            connection = get_connection()            
            sQuery = f"SELECT idale, nombre, descripcion, gravedad, reaccion, paciente_id FROM public.alergia WHERE idale={id};"
            alergia = None
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row:
                    alergia = Alergia(row[0],row[1],row[2],row[3],row[4],row[5])
                    alergia = alergia.to_JSON()
                connection.close()
            return alergia
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_alergia(self, alergia):
        try:
            connection = get_connection()            
            sQuery = f"INSERT INTO public.alergia (nombre, descripcion, gravedad, reaccion, paciente_id) VALUES('{alergia.nombre}', '{alergia.descripcion}', '{alergia.gravedad}', '{alergia.reaccion}', {alergia.paciente_id});"
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
            sQuery = f"UPDATE public.alergia SET nombre='{alergia.nombre}', descripcion='{alergia.descripcion}', gravedad='{alergia.gravedad}', reaccion='{alergia.reaccion}' WHERE idale={alergia.id});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_alergia(self, id):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.alergia WHERE idale={id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
