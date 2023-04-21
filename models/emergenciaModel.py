from database.db import get_connection
from .entities.Emergencia import Emergencia


class EmergenciaModel:
    @classmethod
    def update_emergencia(self, emergencia):
        try:
            connection = get_connection()
            sQuery = f"UPDATE vacuna SET nombre='{emergencia.nombre}', direccion='{emergencia.direccion}', lat={emergencia.lat}, longi={emergencia.long} WHERE idh = {emergencia.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_emergencia(self, emergencia):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.emergencia (fecha, descripcion, id_ambulancia, id_hospital, estado) VALUES(NOW(), '{emergencia.descripcion}', {emergencia.ambulancia_id}, {emergencia.hospital_id}, '{emergencia.estado}');"
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
