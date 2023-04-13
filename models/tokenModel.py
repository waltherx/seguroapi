from database.db import get_connection
from .entities.Token import Token


class TokenModel:
	@classmethod
	def get_token(self, id):
		try:
			connection = get_connection()
			sQuey = f"SELECT t.idt, t.user_id, t.token, t.created_at, t.updated_at FROM public.tokens t, public.usuario u where u.idu = t.user_id and t.user_id = {id};"
			with connection.cursor() as cursor:
				cursor.execute(sQuey)
				row = cursor.fetchone()
				token = None
				if row != None:
					token = Token(row[0], row[1], row[2], row[3], row[4])
					token = token.to_JSON()
			connection.close()
			return token
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def add_token(self, token):
		try:
			connection = get_connection()
			sQuery = f"INSERT INTO public.tokens (user_id, token, created_at, updated_at) VALUES({token.user_id}, '{token.token}', now(), null);"
			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()
			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def update_token(self, token):
		try:
			connection = get_connection()
			sQuery = f"UPDATE public.tokens SET token='{token.token}', updated_at=now() WHERE user_id = {token.user_id} and idt = {token.id};"
			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()
			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def delete_token(self, id):
		try:
			connection = get_connection()
			sQuery = f"DELETE FROM public.tokens WHERE idt = {id};"
			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()
			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)