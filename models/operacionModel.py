from database.db import get_connection
from .entities.Operacion import Operacion


class OperacionModel:
    @classmethod
    def get_operacion(self, ci):
        try:
            sQuery = f"SELECT o.idop, o.tipo, o.fecha, o.descripcion, o.paciente_id FROM operacion o, paciente a ,persona p where p.ci = a.ci_persona and o.paciente_id = a.idpac and p.ci = {ci};"
            connection = get_connection()
            operacions = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    operacion = Operacion(row[0], row[1], row[2], row[3], row[4])
                    operacions.append(operacion.to_JSON())
            connection.close()
            return operacions
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_operacion(self, id):
        try:
            sQuery = f"SELECT idop, tipo, fecha, descripcion, paciente_id FROM public.operacion where = idop{id};"
            connection = get_connection()
            operacion = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchall()
                if row:
                    operacion = Operacion(row[0], row[1], row[2], row[3], row[4])
                    operacion = operacion.to_JSON()
            connection.close()
            return operacion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_operacion(self, operacion):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.operacion (tipo, fecha, descripcion, paciente_id) VALUES('{operacion.tipo}', '{operacion.fecha}', '{operacion.descripcion}', {operacion.paciente_id});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_operacion(self, operacion):
        try:
            connection = get_connection()
            sQuery = f"UPDATE public.operacion SET tipo='{operacion.tipo}', fecha='{operacion.fecha}', descripcion='{operacion.descripcion}' WHERE idop={operacion.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_operacion(self, operacion):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.operacion WHERE idop= {operacion.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
