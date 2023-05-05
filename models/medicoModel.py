from database.db import get_connection
from .entities.Medico import Medico


class MedicoModel:
    @classmethod
    def get_medicosXhospital(self, id):
        try:
            connection = get_connection()
            medicos = []
            sQuey = f"SELECT m.idmed ,m.especialidad ,m.ci_persona ,u.idu ,u.nameuser  FROM public.medico m, usuario u ,public.hospital h where u.ci_persona = m.ci_persona and m.hospital_id  = h.idh and m.hospital_id = {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                resultset = cursor.fetchall()
                for row in resultset:
                    medico = {
                        "id_medico": row[0],
                        "especialidad": row[1],
                        "ci_persona": row[2],
                        "user_id": row[3],
                        "name_user": row[4],
                    }
                    medicos.append(medico)
                connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_medico(self, id):
        try:
            connection = get_connection()
            sQuey = f"SELECT idmed, especialidad, hospital_id, user_id FROM public.medico m where m.idmed =  {id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                medico = None
                if row != None:
                    medico = Medico(row[0], row[1], row[2], row[3])
                    medico = medico.to_JSON()
            connection.close()
            return medico
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_medicos(self):
        try:
            sQuery = f"SELECT * FROM medico"
            connection = get_connection()
            medicos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    medico = Medico(row[0], row[1], row[2], row[3])
                    medicos.append(medico.to_JSON())
                connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_medicos_persons(self):
        try:
            sQuery = f"SELECT  p.ci, m.idmed, p.nombres, p.apellidos, to_char(p.fecha_nacimiento,'DD-MM-YYYY'), p.foto_url, p.foto_name, p.direccion, p.genero, p.estado_civil, m.especialidad, m.hospital_id  FROM persona p, medico m where p.ci = m.ci_persona ORDER BY ci ASC;"
            connection = get_connection()
            medicos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    _medico = {
                        "ci": row[0],
                        "id_medico": row[1],
                        "nombres": row[2],
                        "apellidos": row[3],
                        "fecha_nacimiento": row[4],
                        "foto_url": row[5],
                        "foto_name": row[6],
                        "direccion": row[7],
                        "genero": row[8],
                        "estado_civil": row[9],
                        "especialidad": row[10],
                        "hospital_id": row[11],
                    }
                    medicos.append(_medico)
                connection.close()
            return medicos
        except Exception as ex:
            raise Exception(ex)
