from database.db import get_connection
from .entities.Documento import Documento


class DocumentoModel:
    @classmethod
    def get_documentos(self, ci):
        try:
            sQuery = f"SELECT iddoc,nombre, url, tipo, fecha,ci_persona FROM public.documento, public.persona where persona.ci=documento.ci_persona and documento.ci_persona = {ci};"
            
            connection = get_connection()
            documentos = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    documento = Documento(
                        row[0], row[1], row[2], row[3], None, row[4], row[5]
                    )
                    print(documento.to_JSON())
                    documentos.append(documento.to_JSON())
            connection.close()            
            return documentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_documento(self, documento):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.documento(tipo, url, fecha, ci_persona) VALUES('{documento.tipo}','{documento.url}','{documento.fecha}',{documento.ci})"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_documento(self, documento):
        try:
            connection = get_connection()
            sQuery = f"UPDATE vacuna SET nombre='{documento.nombre}', direccion='{documento.direccion}', lat={documento.lat}, longi={documento.long} WHERE idh = {documento.id}"
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
