# this file is responsible for signing, encoding, decoding and returning JWTs

import time
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')
# JWT_EXPIRATION = config('expiration')


# this function returns the generated tokens (JWTs)
def token_response(token):
    return {
        'access token': token
    }


# this function signs the JWT string
def signed_jwt(userId):
    payload = {
        'user_id': userId,
        'expiry': time.time() + 600
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}


