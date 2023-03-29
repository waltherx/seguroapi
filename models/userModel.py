from database.db import get_connection
from .entities.User import User


class UserModel:
    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario")
                resultset = cursor.fetchall()
                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    users.append(user.to_JSON())
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM usuario WHERE idu = %s", (id))
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyname(self, nameuser):
        try:
            connection = get_connection()
            sQuery = f"SELECT * FROM usuario WHERE nameuser='{nameuser}'"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5])
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO usuario (nameuser, password, email, idrol) VALUES ('{user.nameuser}','{user.password}','{user.email}',{user.idrol})"
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)


"""
    @classmethod
    def update_user(self, hospital):
        try:
            connection = get_connection()
            sQuery = f"UPDATE hospital SET nombre='{hospital.nombre}', direccion='{hospital.direccion}', lat={hospital.lat}, longi={hospital.long} WHERE idh = {hospital.id}"
            print(sQuery)
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, hospital):
        try:
            connection = get_connection()
            sQuery = f"DELETE FROM hospital WHERE idh = {hospital.id}"

            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
"""
