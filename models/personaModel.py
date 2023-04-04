from database.db import get_connection
from .entities.Persona import Persona


class PersonaModel:
    @classmethod
    def get_personas(self):
        try:
            connection = get_connection()
            personas = []
            sQuery = f"SELECT ci, nombres, apellidos, to_char(fechanac,'DD-MM-YYYY'), licvehicular, foto, tiposangre, hipertencion, altura, peso, direccion FROM persona ORDER BY ci ASC;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
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
                        row[9],
                        row[10],
                    )
                    personas.append(persona.to_JSON())
            connection.close()
            return personas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_persona(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT ci, nombres, apellidos, to_char(fechanac,'DD-MM-YYYY'), licvehicular,  foto, tiposangre, hipertencion, altura, peso, direccion FROM persona WHERE ci = {ci} ORDER BY ci ASC;"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()

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
                        row[9],
                        row[10],
                    )
                    persona = persona.to_JSON()

            connection.close()
            return persona
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_persona(self, persona):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO persona (ci, nombres, apellidos, fechanac, licvehicular, foto, tiposangre, hipertencion, altura, peso, direccion) VALUES ({persona.ci},'{persona.nombres}','{persona.apellidos}','{persona.fechaNac}',{persona.licVehicular},'{persona.foto}','{persona.tipoSangre}','{persona.hipertencion}',{persona.altura},{persona.peso},'{persona.direccion}')"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            if affected_rows == 1:
                return persona.ci
            else:
                return 0
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_persona(self, persona):
        try:
            connection = get_connection()
            sQuery = f"UPDATE persona SET nombres='{persona.nombres}', apellidos='{persona.apellidos}', fechanac='{persona.fechaNac}', licvehicular={persona.licVehicular}, foto='{persona.foto}', tipoSangre='{persona.tipoSangre}', hipertencion='{persona.hipertencion}', altura='{persona.altura}', peso='{persona.peso}', direccion='{persona.direccion}' WHERE ci = {persona.ci}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_persona(self, persona):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM persona WHERE idenf = {persona.ci}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
