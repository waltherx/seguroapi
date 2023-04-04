from database.db import get_connection
from .entities.Medicamento import Medicamento


class MedicamentoModel:

    @classmethod
    def get_medicamentos(self):
        try:
            connection = get_connection()
            medicamentos = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM medicamento")
                resultset = cursor.fetchall()
                for row in resultset:
                    medicamento = Medicamento(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    medicamentos.append(medicamento.to_JSON())

            connection.close()
            return medicamentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_medicamento(self, ci):
        try:
            sQuery =f"SELECT idme, nombre, descripcion, cantidad, unidad_medida, ci_persona FROM medicamento,persona where medicamento.ci_persona = persona.ci and persona.ci = {ci};"
            connection = get_connection()
            medicamentos = []

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    medicamento = Medicamento(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    medicamentos.append(medicamento.to_JSON())

            connection.close()
            return medicamentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_medicamento(self, medicamento):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.medicamento(nombre, descripcion, cantidad, unidad_medida, ci_persona) VALUES ('{medicamento.nombre}','{medicamento.descripcion}',{medicamento.cantidad},{medicamento.unidad}, {medicamento.ci})"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_medicamento(self, medicamento):
        try:
            connection = get_connection()
            sQuery = f"UPDATE medicamento SET nombre='{medicamento.nombre}', direccion='{medicamento.direccion}', lat={medicamento.lat}, longi={medicamento.long} WHERE idh = {medicamento.id}"
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
    def delete_medicamento(self, medicamento):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM medicamento WHERE idh = {medicamento.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
