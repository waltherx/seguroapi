from database.db import get_connection
from .entities.Phone import Phone


class PhoneModel:
    """
    @classmethod
    def get_phones(self, id):
        try:
            connection = get_connection()
            phones = []
            sQuery = f"SELECT t.idp, t.numero, t.referencia, t.ci_persona FROM phone t, persona p where t.ci_persona = p.ci and t.ci_persona ={ id } ORDER BY t.idp ASC;"
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
    """
    @classmethod
    def get_phone(self, ci):
        try:
            connection = get_connection()
            sQuery = f"SELECT t.idp, t.numero, t.referencia, t.ci_persona FROM phone t, persona p where t.ci_persona = p.ci and t.ci_persona ={ci} ORDER BY t.idp ASC"
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
    def get_phone_by(self, ci, id):
        try:
            connection = get_connection()
            sQuery = f"SELECT t.idp, t.numero, t.referencia, t.ci_persona FROM phone t JOIN persona p ON t.ci_persona = p.ci WHERE t.ci_persona = {ci} AND t.idp = {id} LIMIT 1;"
            phone = None
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                if row != None:
                    phone = Phone(row[0], row[1], row[2], row[3])
                    phone = phone.to_JSON()
            connection.close()
            return phone
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_phone(self, phone):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.phone (numero, referencia, ci_persona) VALUES ('{phone.numero}','{phone.referencia}',{phone.ci_persona})"
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
            sQuery = f"UPDATE public.phone SET numero='{phone.numero}', referencia='{phone.referencia}' WHERE idp={phone.id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_phone(self, id):
        try:
            connection = get_connection()
            sQuery=f"DELETE FROM public.phone WHERE idp={id};"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
