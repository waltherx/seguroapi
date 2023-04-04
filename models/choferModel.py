from database.db import get_connection
from .entities.Chofer import Chofer

class ChoferModel:

    @classmethod
    def get_chofer(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idch, licencia, categoria, estado, id_ambulancia FROM public.chofer where idch = {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                chofer = None
                if row != None:
                    chofer = Chofer(row[0], row[1], row[2], row[3], row[4])
                    chofer = chofer.to_JSON()
            connection.close()
            return chofer
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_chofersxId(self, id):
        try:
            sQuery = f"SELECT idch, licencia, categoria, estado, id_ambulancia FROM public.chofer, public.ambulancia  where chofer.id_ambulancia = ambulancia.idam  and chofer.id_ambulancia =  {id};"
            connection = get_connection()
            chofers = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    chofer = Chofer(row[0], row[1], row[2], row[3], row[4])
                    chofers.append(chofer.to_JSON())
                connection.close()
            return chofers
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_chofers(self):
        try:
            sQuery = f"SELECT idch, licencia, categoria, estado, id_ambulancia FROM chofer"
            connection = get_connection()
            chofers = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    chofer = Chofer(row[0], row[1], row[2], row[3], row[4])
                    chofers.append(chofer.to_JSON())
                connection.close()
            return chofers
        except Exception as ex:
            raise Exception(ex)
