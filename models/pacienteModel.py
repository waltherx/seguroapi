from database.db import get_connection
from .entities.Persona import Persona
from .entities.Paciente import Paciente


class PacienteModel:
    @classmethod
    def get_pacientes(self):
        try:
            connection = get_connection()
            pacientes = []
            sQuery = f"SELECT idpac, tiposangre, hipertencion, altura, peso, ci_persona FROM public.paciente;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    paciente = Paciente(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                    )
                    pacientes.append(paciente.to_JSON())
            connection.close()
            return pacientes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paciente_X_ci(self, ci):
        try:
            connection = get_connection()
            
            sQuery = f"select ci, nombres, apellidos, to_char(fecha_nacimiento,'DD-MM-YYYY'), foto_url, foto_name, direccion, genero, idpac, tiposangre, hipertencion, altura, peso, ci_persona FROM public.persona p, public.paciente c where p.ci = c.ci_persona and p.ci = {ci} ;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                persona = None
                paciente = None
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
                    )
                    
                    paciente = Paciente(
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                    )
                    persona = persona.to_JSON()                    
                    paciente = paciente.to_JSON()
            connection.close()
            return {"paciente": paciente, "persona": persona}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_paciente(self, paciente):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO persona (ci, nombres, apellidos, fechanac, licvehicular, foto, tiposangre, hipertencion, altura, peso, direccion) VALUES ({persona.ci},'{persona.nombres}','{persona.apellidos}','{persona.fechaNac}',{persona.licVehicular},'{persona.foto}','{persona.tipoSangre}','{persona.hipertencion}',{persona.altura},{persona.peso},'{persona.direccion}')"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            if affected_rows == 1:
                return 1
            else:
                return 0
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_paciente(self, paciente):
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
    def delete_paciente(self, paciente):
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
