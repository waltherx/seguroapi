from database.db import get_connection
from .entities.User import User, UserLogged
from .entities.Rol import Rol
from werkzeug.security import generate_password_hash


class UserModel:
    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []
            sQuery = f"select u.idu ,p.ci, u.nameuser, CONCAT(p.apellidos  ,', ', p.nombres) AS nombre_completo, r.nombre  from persona p ,usuario u ,rol r where p.ci =u.ci_persona and u.idrol  =r.idrol order by u.idu asc"
            with connection.cursor() as cursor:
                cursor.execute(sQuery)
                resultset = cursor.fetchall()
                for row in resultset:
                    user = {
                        "id_user": row[0],
                        "ci_persona": row[1],
                        "name_user": row[2],
                        "nombre_completo": row[3],
                        "rol": row[4],
                    }
                    users.append(user)
            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(self, user: User):
        try:
            cursor = get_connection().cursor()
            sQuery = f"SELECT u.idu ,u.nameuser ,u.email ,u.password  ,p.ci ,p.nombres ,p.apellidos ,p.foto_url, u.idrol from persona p , usuario u where p.ci = u.ci_persona and u.nameuser  = '{user.nameuser}' limit 1;"
            cursor.execute(sQuery)
            row = cursor.fetchone()
            if row != None:
                coincide = User.verificar_password(row[3], user.password)
                if coincide:
                    usuario_logeado = UserLogged(
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
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def view_user(self, id: int) -> dict:
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sQuey = f"SELECT u.idu ,u.nameuser ,u.email ,u.password  ,p.ci , p.nombres , p.apellidos , p.foto_url, u.idrol from persona p , usuario u where p.ci = u.ci_persona and u.idu  = {id} limit 1;"
                cursor.execute(sQuey)
                row = cursor.fetchone()
                user_logged = None
                if row != None:
                    user_logged = UserLogged(
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
            connection.close()
            return user_logged
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sQuey = f"SELECT * FROM usuario WHERE idu = {id};"
                cursor.execute(sQuey)
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = User(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                    )
                    # user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sQuey = f"SELECT u.idu, u.nameuser, u.password, u.email, u.estado, u.token, u.idrol, u.ci_persona, p.nombres , p.apellidos , p.foto_url , p.foto_name  FROM usuario u ,persona p where p.ci =u.ci_persona and u.idu = {id};"
                cursor.execute(sQuey)
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = {
                        "id": row[0],
                        "nameuser": row[1],
                        "password": row[2],
                        "email": row[3],
                        "estado": row[4],
                        "token": row[5],
                        "idrol": row[6],
                        "ci_persona": row[7],
                        "nombres": row[8],
                        "apellidos": row[9],
                        "foto_url": row[10],
                        "foto_name": row[11],
                    }
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
                    user = User(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                    )
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()
            sQuery = f"INSERT INTO public.usuario (nameuser, password, email, estado, idrol, ci_persona) VALUES('{user.nameuser}', '{generate_password_hash(user.password)}', '{user.email}', 'act', {user.idrol}, {user.ci_persona});"
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

    @classmethod
    def get_user_by_ci(self, ci):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sQuery = f"SELECT p.ci, p.nombres, p.apellidos, p.fecha_nacimiento, p.foto_url, p.foto_name, p.direccion, p.genero, p.estado_civil, u.idu, u.nameuser, u.password, u.email, u.estado, u.token, idrol FROM persona p ,usuario u where p.ci = u.ci_persona and p.ci =  {ci};"
                cursor.execute(sQuery)
                row = cursor.fetchone()
                user = None
                if row != None:
                    user = {
                        "ci": row[0],
                        "nombres": row[1],
                        "apellidos": row[2],
                        "fecha_nacimiento": row[3],
                        "foto_url": row[4],
                        "foto_name": row[5],
                        "direccion": row[6],
                        "genero": row[7],
                        "estado_civil": row[8],
                        "idu": row[9],
                        "nameuser": row[10],
                        "password": row[11],
                        "email": row[12],
                        "estado": row[13],
                        "token": row[14],
                        "idrol": row[15],
                    }
                    # user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)
