from database.db import get_connection
from .entities.Ambulancia import Ambulancia


class AmbulanciaModel:
    @classmethod
    def get_ambulancia(self):
        try:
            connection = get_connection()
            ambulancias = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ambulancia;")
                resultset = cursor.fetchall()
                for row in resultset:
                    ambulancia = Ambulancia(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                    )
                    ambulancias.append(ambulancia.to_JSON())
            connection.close()
            return ambulancias
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ambulanciaId(self, id: int):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ambulancia WHERE idam = %s", (id))
                row = cursor.fetchone()
                ambulancia = None
                if row != None:
                    ambulancia = Ambulancia(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                    )
                    ambulancia = ambulancia.to_JSON()
            connection.close()
            return ambulancia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ambulanciaIdchofer(self, id):
        try:
            connection = get_connection()
            sQuery = f"SELECT a.idam, a.modelo, a.marca, a.anio, a.placa, a.capcidad, a.lat, a.longi, a.estado FROM ambulancia a , chofer c where a.idam = c.id_ambulancia and c.idch = {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                ambulancia = None
                if row != None:
                    ambulancia = Ambulancia(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                    )
                    ambulancia = ambulancia.to_JSON()
            connection.close()
            return ambulancia
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_ambulancia(self, ambulancia):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.ambulancia (modelo, marca, anio, placa, capcidad) VALUES('{ambulancia.modelo}', '{ambulancia.marca}', {ambulancia.anio}, '{ambulancia.placa}', {ambulancia.capacidad});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_ambulancia(self, ambulancia):
        try:
            connection = get_connection()
            sQuery = f"UPDATE public.ambulancia SET modelo='{ambulancia.modelo}', marca='{ambulancia.marca}', anio={ambulancia.anio}, placa='{ambulancia.placa}', capcidad={ambulancia.capacidad} WHERE idam={ambulancia.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_location(self, ambulancia):
        try:
            connection = get_connection()
            sQuery = f"UPDATE ambulancia SET lat = {ambulancia.lat}, longi = {ambulancia.long} WHERE idam = {ambulancia.id}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
