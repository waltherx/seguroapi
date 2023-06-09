from database.db import get_connection
from .entities.Persona import Persona
from .entities.Paciente import Paciente


class PacienteModel:
    @classmethod
    def get_pacs(self):
        try:
            connection = get_connection()
            pacs = []
            sQuery = f"select * from persona p,paciente a where p.ci = a.ci_persona order by a.idpac asc;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                pac = None
                for row in resultset:
                    pac = {
                        "ci_persona": row[0],
                        "nombres": row[1],
                        "apellidos": row[2],
                        "fecha_nacimiento": row[3],
                        "foto_url": row[4],
                        "foto_name": row[5],
                        "direccion": row[6],
                        "genero": row[7],
                        "estado_civil": row[8],
                        "id_paciente": row[9],
                        "tipo_sangre": row[10],
                        "hipertencion": row[11],
                        "altura": row[12],
                        "peso": row[13],
                    }
                    pacs.append(pac)
                connection.close()
            return pacs
        except Exception as ex:
            raise Exception(ex)

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
    def get_paciente_new(self, id):
        try:
            connection = get_connection()
            sQuery = f"select ci, nombres, apellidos, to_char(fecha_nacimiento,'DD-MM-YYYY'), foto_url, foto_name, direccion, genero, idpac, tiposangre, hipertencion, altura, peso, ci_persona FROM public.persona p, public.paciente c where p.ci = c.ci_persona and p.ci = {id} ;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                persona = None
                paciente = None
                if row != None:
                    paciente = {
                        "ci": row[0],
                        "nombres": row[1],
                        "apellidos": row[2],
                        "fecha_nacimiento": row[3],
                        "foto_url": row[4],
                        "foto_name": row[5],
                        "direccion": row[6],
                        "genero": row[7],
                        "id_paciente": row[8],
                        "tiposangre": row[9],
                        "hipertencion": row[10],
                        "altura": row[11],
                        "peso": row[12],
                    }
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_paciente(self, id: int):
        try:
            connection = get_connection()
            sQuery = f"SELECT idpac, tiposangre, hipertencion, altura, peso, ci_persona FROM public.paciente where idpac ={id} limit  1;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                paciente = None
                if row != None:
                    paciente = {
                        "id": row[0],
                        "tipo_sangre": row[1],
                        "hipertencion": row[2],
                        "altura": row[3],
                        "peso": row[4],
                    }
            connection.close()
            return paciente
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_paciente_X_ci(self, ci :int):
        try:
            connection = get_connection()
            sQuery = f"select p.ci, p.nombres, p.apellidos, to_char(p.fecha_nacimiento,'YYYY-MM-DD'), p.foto_url, p.foto_name, p.direccion, p.genero, p.estado_civil, c.idpac, c.tiposangre, c.hipertencion, c.altura, c.peso, c.ci_persona FROM public.persona p, public.paciente c where p.ci = c.ci_persona and p.ci = {ci} ;"
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
                        row[8],
                    )

                    paciente = Paciente(
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14],
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
            sQuery = f"INSERT INTO public.paciente (tiposangre, hipertencion, altura, peso, ci_persona) VALUES('{paciente.tipoSangre}', '{paciente.hipertencion}', {paciente.altura}, {paciente.peso}, {paciente.ci_persona});"
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
            sQuery = f"UPDATE public.paciente SET tiposangre='{paciente.tipoSangre}', hipertencion='{paciente.hipertencion}', altura={paciente.altura}, peso={paciente.peso} WHERE idpac={paciente.id};"

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
