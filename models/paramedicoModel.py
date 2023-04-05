from database.db import get_connection
from .entities.Paramedico import Paramedico


class ParamedicoModel:
    
    @classmethod
    def get_paramedicosA(self):
        try:
            sQuery = f"SELECT * FROM public.paramedico;"
            connection = get_connection()
            paramedicos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    paramedico = Paramedico(row[0], row[1], row[2])
                    paramedicos.append(paramedico.to_JSON())
                connection.close()
            return paramedicos
        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def get_paramedico(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idpar, especialidad, id_ambulancia FROM public.paramedico where paramedico.idpar =  {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                paramedico = None
                if row != None:
                    paramedico = Paramedico(row[0], row[1], row[2])
                    paramedico = paramedico.to_JSON()
            connection.close()
            return paramedico
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paramedicos(self, id):
        try:
            sQuery = f"SELECT idpar, especialidad, id_ambulancia FROM public.paramedico,public.ambulancia where paramedico.id_ambulancia  = ambulancia.idam  and ambulancia.idam = {id};"
            connection = get_connection()
            paramedicos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    paramedico = Paramedico(row[0], row[1], row[2])
                    paramedicos.append(paramedico.to_JSON())
                connection.close()
            return paramedicos
        except Exception as ex:
            raise Exception(ex)
