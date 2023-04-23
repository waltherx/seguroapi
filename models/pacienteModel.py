from database.db import get_connection
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
    def get_paciente(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT ci, nombres, apellidos, to_char(fechanac,'DD-MM-YYYY'), licvehicular,  foto, tiposangre, hipertencion, altura, peso, direccion,user_id FROM persona WHERE ci = {ci} ORDER BY ci ASC;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                paciente = None
                if row != None:
                    paciente = Paciente(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                    )
                    paciente = paciente.to_JSON()
            connection.close()
            return paciente
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
