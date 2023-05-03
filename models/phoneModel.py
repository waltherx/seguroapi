from database.db import get_connection
from .entities.Phone import Phone


class PhoneModel:
    @classmethod
    def get_phones(self):
        try:
            connection = get_connection()
            phones = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT idp, numero, referencia, ci_persona FROM public.phone ORDER BY idp ASC"
                )
                resultset = cursor.fetchall()

                for row in resultset:
                    phone = Phone(row[0], row[1], row[2], row[3])
                    phones.append(phone.to_JSON())

            connection.close()
            return phones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_phone(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT d.iddoc, d.tipo, d.url, d.fecha, d.nombre, d.paciente_id FROM documento d, paciente a, persona p where p.ci = a.ci_persona and a.idpac = d.paciente_id and p.ci ={ci};"
            phones = []
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    phone = Phone(row[0], row[1], row[2], row[3])
                    phones.append(phone.to_JSON())
            connection.close()
            return phones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_phone(self, phone):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.phone (numero, referencia, ci_persona) VALUES ('{phone.id}','{phone.numero}',{phone.ci})"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_phone(self, phone):
        try:
            connection = get_connection()

            sQuery = f"UPDATE public.phone SET numero='{phone.numero}', referencia='{phone.referencia}' WHERE idp={phone.idp});"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_phone(self, phone):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM phone WHERE idp = %s", (phone.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
