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
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
                    )
                    ambulancias.append(ambulancia.to_JSON())
            connection.close()
            return ambulancias
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_ambulanciaId(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM ambulancia WHERE idam = %s", (id))
                row = cursor.fetchone()
                ambulancia = None
                if row != None:
                    ambulancia = Ambulancia(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8]
                    )
                    ambulancia = ambulancia.to_JSON()
            connection.close()
            return ambulancia
        except Exception as ex:
            raise Exception(ex)
        
  
            