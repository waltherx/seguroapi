from database.db import get_connection
from werkzeug.exceptions import BadRequest
from .entities.Medicamento import Medicamento


class MedicamentoModel:
    @classmethod
    def view_medicamentos(self, id: int):
        try:
            connection = get_connection()
            medicamento = None
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM medicamento where idme={id};")
                row = cursor.fetchone()
                if row:
                    medicamento = Medicamento(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    medicamento = medicamento.to_JSON()
            connection.close()
            return medicamento
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_medicamento(self, ci: int):
        try:
            sQuery = f"SELECT m.idme, m.nombre, m.descripcion, m.cantidad, m.unidad_medida, m.paciente_id FROM medicamento m, paciente a, persona p where p.ci = a.ci_persona and m.paciente_id =a.idpac and p.ci = {ci} order by m.idme asc;"
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
    def add_medicamento(self, medicamento: Medicamento):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.medicamento (nombre, descripcion, cantidad, unidad_medida, paciente_id) VALUES('{medicamento.nombre}', '{medicamento.descripcion}', {medicamento.cantidad}, '{medicamento.unidad}', {medicamento.paciente_id});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_medicamento(self, medicamento: Medicamento):
        try:
            connection = get_connection()
            sQuery = f"UPDATE public.medicamento SET nombre='{medicamento.nombre}', descripcion='{medicamento.descripcion}', cantidad={medicamento.cantidad}, unidad_medida='{medicamento.unidad}' WHERE idme= {medicamento.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_medicamento(self, id: int):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM public.medicamento WHERE idme={id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
