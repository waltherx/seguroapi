from database.db import get_connection
from .entities.Emergencia import Emergencia

class EmergenciaModel:
    
    @classmethod
    def get_emergencia(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idem, fecha, descripcion, id_ambulancia, id_hospital, estado FROM public.emergencia where idem =  %s",(id,)
                )
                row = cursor.fetchone()
                emergencia = None
                if row != None:
                    emergencia = Emergencia(row[0], row[1], row[2], row[3], row[4], row[5])
                    emergencia = emergencia.to_JSON()
            connection.close()
            return emergencia
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_emergencia(self, emergencia):
        try:
            connection = get_connection()
            sQuery = f"UPDATE emergencia SET estado='{emergencia.estado}' WHERE idem = {emergencia.id}"
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
