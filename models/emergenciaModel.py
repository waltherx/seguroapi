from database.db import get_connection
from .entities.Emergencia import Emergencia


class EmergenciaModel:
    @classmethod
    def get_emergencia(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idem, fecha, descripcion, estado, id_ambulancia, id_hospital FROM public.emergencia where idem =  %s",
                    (id,),
                )
                row = cursor.fetchone()
                emergencia = None
                if row != None:
                    emergencia = Emergencia(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    emergencia = emergencia.to_JSON()
            connection.close()
            return emergencia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_emergencias_x_ambulancia(self, id):
        try:
            connection = get_connection()
            sQuery = f"select e.idem, e.fecha, e.descripcion, e.estado ,e.id_ambulancia, e.id_hospital  from emergencia e ,ambulancia a where e.id_ambulancia = a.idam and a.idam = {id};"
            emergencias = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    emergencia = Emergencia(
                        row[0], row[1], row[2], row[3], row[4], row[5]
                    )
                    emergencias.append(emergencia.to_JSON())
            connection.close()
            return emergencias
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
            sQuery = f"INSERT INTO public.emergencia (fecha, descripcion, id_ambulancia, id_hospital, estado) VALUES(now() AT TIME ZONE 'America/La_Paz', '{emergencia.descripcion}', {emergencia.ambulancia_id}, {emergencia.hospital_id}, '{emergencia.estado}');"
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
