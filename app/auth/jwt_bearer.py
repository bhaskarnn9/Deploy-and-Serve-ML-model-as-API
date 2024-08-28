# the objective of this file is to check whether the request is authorized or not
# in other words, verification of the protected route

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decode_jwt


class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Invalid or expired token')
            else:
                return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid or expired token')

    @staticmethod
    def verify_token(jw_token: str):
        is_token_valid: bool = False
        payload = decode_jwt(jw_token)
        if payload:
            is_token_valid = True
        return is_token_valid
