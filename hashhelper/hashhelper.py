from bcrypt import checkpw, hashpw, gensalt
from sqlalchemy import false

class HashHelper(object):
    @staticmethod
    def verify_method(plain_password: str, hashed_password: str):
        if checkpw(plain_password.encode("utf-8"),hashed_password.encode("utf-8")):
            return True;
        else:
            return False;

    @staticmethod
    def get_passowrd_hash(plain_password : str):
        return hashpw(plain_password.encode('utf-8'),gensalt()).decode('utf-8')