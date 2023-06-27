from database.db import get_connection
from .entities.Persona import Persona


class PersonaModel:
    @classmethod
    def get_personas(self):
        try:
            connection = get_connection()
            personas = []
            sQuery = f"SELECT  p.ci, a.idpac, p.nombres, p.apellidos, to_char(p.fecha_nacimiento,'DD-MM-YYYY'), p.foto_url, p.foto_name, p.direccion, p.genero, p.estado_civil, a.tiposangre, a.hipertencion, a.altura, a.peso FROM persona p, paciente a where p.ci = a.ci_persona ORDER BY ci ASC;"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    _persona = {
                        "ci": row[0],
                        "id_paciente": row[1],
                        "nombres": row[2],
                        "apellidos": row[3],
                        "fecha_nacimiento": row[4],
                        "foto_url": row[5],
                        #"foto_name": row[6],
                        "direccion": row[7],
                        "genero": row[8],
                        "esdo_civil": row[9],
                        "tipo_sangre": row[10],
                        "hipertencion": row[11],
                        "altura": row[12],
                        "peso": row[13],
                    }
                    
                    print(row[12])
                    print('------------------------------------')   
                    print(row[13])
                    personas.append(_persona)
            connection.close()
            return personas
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_persona(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT ci, nombres, apellidos, to_char(fecha_nacimiento,'DD-MM-YYYY'), foto_url, foto_name, direccion, genero, estado_civil FROM persona WHERE ci = {ci};"
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
                    )
                    persona = persona.to_JSON()
            connection.close()
            return persona
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def view_persona(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT ci, nombres, apellidos, to_char(fecha_nacimiento, 'YYYY-MM-DD'), foto_url, foto_name, direccion, genero, estado_civil FROM public.persona where ci={ci};"
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
                        row[8]
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
            sQuery = f"INSERT INTO public.persona (ci, nombres, apellidos, fecha_nacimiento, direccion, genero, estado_civil) VALUES({persona.ci}, '{persona.nombres}', '{persona.apellidos}' , '{persona.fecha_nacimiento}', '{persona.direccion}', '{persona.genero}', '{persona.estado_civil}');"
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
    def update_persona(self, persona:Persona)-> int:
        try:
            connection = get_connection()
            sQuery = f"UPDATE persona SET  nombres='{persona.nombres}', apellidos='{persona.apellidos}', fecha_nacimiento='{persona.fecha_nacimiento}', direccion='{persona.direccion}', genero='{persona.genero}', estado_civil='{persona.estado_civil}' WHERE ci = {persona.ci};"
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

    @classmethod
    def upload_photo(self, persona):
        try:
            connection = get_connection()
            sQuery = f"UPDATE persona SET foto_url='{persona.foto_url}', foto_name='{persona.foto_name}' WHERE ci = {persona.ci}"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
