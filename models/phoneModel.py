from database.db import get_connection
from .entities.Phone import Phone


class PhoneModel:
    @classmethod
    def get_phones(self):
        try:
            connection = get_connection()
            phones = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT idp, numero FROM phone ORDER BY idp ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    phone = Phone(row[0], row[1])
                    phones.append(phone.to_JSON())

            connection.close()
            return phones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_phone(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, numero FROM phone WHERE idp = %s", (id,))
                row = cursor.fetchone()

                movie = None
                if row != None:
                    phone = Phone(row[0], row[1])
                    phone = phone.to_JSON()

            connection.close()
            return phone
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_phone(self, phone):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO phone (idp, numero)                                  
                                VALUES (%s,%s)""",
                    (phone.id, phone.numero),
                )
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

            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE phone SET numero = %s
                                WHERE idp = %s""",
                    (phone.numero),
                )
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
