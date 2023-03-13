from decouple import config

#SECRET_KEY=SECRET_KEY
#PGSQL_HOST=localhost
#PGSQL_USER=postgres
#PGSQL_PASSWORD=123456
#PGSQL_DB=seguro

class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}