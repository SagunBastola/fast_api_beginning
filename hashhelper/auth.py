import jwt
from decouple import config
import time
JWT_SECRET=config("JWT_SECRET")
JWT_ALGORITHM= config("JWT_ALGORITHM")

def sign_jwt(user_id : int) -> str :
    payload={"user_id" : user_id ,
             "expires" : time.time}
    token= jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token

def decode_jwt(token : str)->dict:
    try : 
        decoded_token=jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        return decoded_token if decoded_token['expires'] >= time.time else None
        
    except:
        print("Not Available")