from database.db import get_connection
from .entities.Hospital import Hospital


class HospitalModel:
    @classmethod
    def get_hospitals(self):
        try:
            connection = get_connection()
            hospitals = []

            with connection.cursor() as cursor:
                cursor.execute("select * from hospital h order by idh asc;")
                resultset = cursor.fetchall()
                for row in resultset:
                    hospital = Hospital(row[0], row[1], row[2], row[3], row[4])
                    hospitals.append(hospital.to_JSON())

            connection.close()
            return hospitals
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_hospital(self, id: int):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM hospital WHERE idh = {id}")
                row = cursor.fetchone()
                hospital = None
                if row != None:
                    hospital = Hospital(row[0], row[1], row[2], row[3], row[4])
                    hospital = hospital.to_JSON()
            connection.close()
            return hospital
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_hospital(self, hospital):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO hospital (nombre, direccion, lat, longi) VALUES ('{hospital.nombre}','{hospital.direccion}',{hospital.lat},{hospital.long})"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_hospital(self, hospital):
        try:
            connection = get_connection()
            sQuery = f"UPDATE hospital SET nombre='{hospital.nombre}', direccion='{hospital.direccion}', lat={hospital.lat}, longi={hospital.long} WHERE idh = {hospital.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_hospital(self, hospital):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM hospital WHERE idh = {hospital.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
