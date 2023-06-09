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
            sQuey = f"select m.idmed, m.ci_persona, p.nombres ,p.apellidos ,p.foto_url ,m.especialidad , m.hospital_id, h.nombre  from medico m, persona p, hospital h where m.ci_persona = p.ci and m.hospital_id =h.idh  and m.idmed = {id} LIMIT 1;"
            with connection.cursor() as cursor:
                cursor.execute(sQuey)
                row = cursor.fetchone()
                medico = None
                if row != None:
                    medico = {
                        "id_medico": row[0],
                        "ci_persona": row[1],
                        "nombres": row[2],
                        "apellidos": row[3],
                        "foto_url": row[4],
                        "especialidad": row[5],
                        "hospital_id": row[6],
                        "hospital_name": row[7],
                    }
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
    def add_medico(self, medico):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.medico (especialidad, hospital_id, ci_persona) VALUES('{medico.especialidad}', {medico.hospital_id}, {medico.ci_persona});"
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
    def update_medico(self, medico: Medico):
        try:
            connection = get_connection()
            sQuery = f"UPDATE public.medico SET especialidad='{medico.especialidad}', hospital_id={medico.hospital_id} WHERE idmed={medico.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return 1 if affected_rows == 1 else 0
        except Exception as xx:
            raise Exception(xx)

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
