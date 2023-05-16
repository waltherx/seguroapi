from database.db import get_connection
from .entities.Persona import Persona
from .entities.Chofer import Chofer


class ChoferModel:
    @classmethod
    def get_chofer(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idch, licencia, categoria, estado, id_ambulancia,ci_persona FROM public.chofer where idch = {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                chofer = None
                if row != None:
                    chofer = Chofer(row[0], row[1], row[2], row[3], row[4], row[5])
                    chofer = chofer.to_JSON()
            connection.close()
            return chofer
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_chofer_x_ci(self, ci):
        try:
            connection = get_connection()
            sQuey = f"select ci, nombres, apellidos, fecha_nacimiento, foto_url, foto_name, direccion, genero, estado_civil, idch, licencia, categoria, estado, id_ambulancia, ci_persona FROM public.chofer c,public.persona p where p.ci = c.ci_persona and p.ci = {ci};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                chofer = None
                persona = None
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
                    persona = persona.to_JSON()
                    chofer = Chofer(row[9], row[10], row[11], row[12], row[13], row[14])
                    chofer = chofer.to_JSON()
            connection.close()
            return {"persona": persona, "chofer": chofer}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_chofersxId(self, id):
        try:
            sQuery = f"SELECT c.idch, c.licencia, c.categoria, c.estado, c.id_ambulancia, c.ci_persona, u.idu FROM chofer c, ambulancia a,usuario u  where c.id_ambulancia = a.idam and u.ci_persona = c.ci_persona  and c.id_ambulancia = {id} and u.idrol = 3;"
            connection = get_connection()
            chofers = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    chofer = {
                        "id_chofer": row[0],
                        "licencia": row[1],
                        "categoria": row[2],
                        "estado": row[3],
                        "id_ambulancia": row[4],
                        "ci_persona": row[5],
                        "user_id": row[6],
                    }
                    chofers.append(chofer)
                connection.close()
            return chofers
        except Exception as ex:
            raise Exception(ex)
        

    @classmethod
    def get_chofers(self):
        try:
            sQuery = f"SELECT idch, licencia, categoria, estado, id_ambulancia, ci_persona FROM chofer"
            connection = get_connection()
            chofers = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    chofer = Chofer(row[0], row[1], row[2], row[3], row[4], row[5])
                    chofers.append(chofer.to_JSON())
                connection.close()
            return chofers
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def get_chofers_persons(self):
        try:
            sQuery = f"SELECT c.idch, p.ci, p.nombres, p.apellidos, p.foto_url, c.licencia, c.categoria, c.estado, c.id_ambulancia FROM persona p,chofer c where p.ci =c.ci_persona;"
            connection = get_connection()
            chofers = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    _chofer = {"idch":row[0],
                              "ci":row[1],
                              "nombre":row[2],
                              "apellido":row[3],
                              "foto_url":row[4],
                              "licencia":row[5],
                              "categoria":row[6],
                              "estado":row[7],
                              "id_ambulancia":row[8],
                    }
                    chofers.append(_chofer)
                connection.close()
            return chofers
        except Exception as ex:
            raise Exception(ex)
        