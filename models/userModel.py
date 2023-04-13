from database.db import get_connection
from .entities.User import User
from .entities.Rol import Rol
from werkzeug.security import generate_password_hash


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
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    users.append(user.to_JSON())
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(self, usuario):
        try:
            cursor = get_connection().cursor()
            sql = """SELECT p.idu, p.nameuser, p.password, p.email, p.estado, p.token, idrol
                    FROM public.usuario p WHERE p.nameuser = '{0}'""".format(
                usuario.nameuser
            )
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = User.verificar_password(data[2], usuario.password)
                if coincide:
                    usuario_logeado = User(
                        data[0], data[1], data[2], data[3], data[4], data[5], data[6]
                    )
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        connection = get_connection()
        with connection.cursor() as cursor:
            sQuey = f"SELECT p.idu, p.nameuser, p.password, p.email, p.estado, p.token, r.idrol ,r.nombre  FROM public.usuario p,public.rol r where p.idrol  = r.idrol and p.idu = {id};"
            cursor.execute(sQuey)
            row = cursor.fetchone()
            user = None
            if row != None:
                user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        connection.close()
        return user

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
                    user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
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

    @classmethod
    def update_user(self, user):
        try:
            conneection = get_connection()
            _pass = generate_password_hash(user.password)
            sQuery = f"UPDATE public.usuario SET nameuser='{user.nameuser}', password='{_pass}', email='{user.email}', estado='{user.estado}' , token='{user.token}', idrol={user.idrol} WHERE idu={user.id};"
            with conneection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                conneection.commit()
            conneection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user_token(self, user):
        try:
            conneection = get_connection()
            sQuery = (
                f"UPDATE public.usuario SET token='{user.token}' WHERE idu={user.id};"
            )
            with conneection.cursor() as cursor:
                cursor.execute(sQuery)
                affected_rows = cursor.rowcount
                conneection.commit()
            conneection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
