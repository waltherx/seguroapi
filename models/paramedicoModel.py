from database.db import get_connection
from .entities.Persona import Persona
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
                    paramedico = Paramedico(row[0], row[1], row[2], row[3])
                    paramedicos.append(paramedico.to_JSON())
                connection.close()
            return paramedicos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paramedicoXci(self, ci):
        try:
            connection = get_connection()
            sQuery = f"select ci, nombres, apellidos, fecha_nacimiento, foto_url, foto_name, direccion, genero, estado_civil, idpar, especialidad, id_ambulancia, ci_persona FROM public.paramedico p , public.persona e where e.ci = ci_persona and e.ci = '{ci}';"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                persona = None
                paramedico = None
                if row != None:
                    persona = Persona(
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
                    paramedico = Paramedico(row[9], row[10], row[11],row[12]	)
                    persona = persona.to_JSON()
                    paramedico = paramedico.to_JSON()
            connection.close()
            return {"persona": persona, "paramedico": paramedico}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paramedico(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idpar, especialidad, id_ambulancia, user_id FROM public.paramedico where paramedico.idpar =  {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                paramedico = None
                if row != None:
                    paramedico = Paramedico(row[0], row[1], row[2], row[3])
                    paramedico = paramedico.to_JSON()
            connection.close()
            return paramedico
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paramedicos(self, id):
        try:
            sQuery = f"SELECT idpar, especialidad, id_ambulancia, user_id FROM public.paramedico,public.ambulancia where paramedico.id_ambulancia  = ambulancia.idam  and ambulancia.idam = {id};"
            connection = get_connection()
            paramedicos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    paramedico = Paramedico(row[0], row[1], row[2], row[3])
                    paramedicos.append(paramedico.to_JSON())
                connection.close()
            return paramedicos
        except Exception as ex:
            raise Exception(ex)
