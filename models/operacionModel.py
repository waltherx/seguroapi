from database.db import get_connection
from .entities.Operacion import Operacion


class OperacionModel:
    @classmethod
    def get_operacion(self, ci):
        try:
            sQuery = f"SELECT idop, tipo, fecha, descripcion, ci_persona FROM persona, operacion where persona.ci = operacion.ci_persona and persona.ci = {ci};"
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
    def add_operacion(self, operacion):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.operacion (tipo, fecha, descripcion, ci_persona) VALUES('{operacion.tipo}','{operacion.fecha}','{operacion.descripcion}',{operacion.ci})"
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
            sQuery = f"UPDATE vacuna SET nombre='{operacion.nombre}', direccion='{operacion.direccion}', lat={operacion.lat}, longi={operacion.long} WHERE idh = {operacion.id}"
            print(sQuery)
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
            sQuery = f"DELETE FROM vacuna WHERE idh = {operacion.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
