from run import bcrypt

def encriptar(_pass):
    return bcrypt.generate_password_hash(_pass).decode("utf-8")