from datetime import datetime
from django.shortcuts import render
from libs.format import hash_secret
from libs.random import random_str
from .cookie import setCookie
import jwt, uuid, math

# Create and Manage your JWT Session here.
class Session:
    __SECRET_KEY = 'secret'

    def _loader(self, request, context):
        if 'SSKY' in request.COOKIES and 'SSID' in request.COOKIES:
            status, pl = self.getJWT(request.COOKIES['SSID'])

            if status == 200:
                # session is ok.
                response = render(request, 'index.html', context)
                return response

            if status == 410:
                # session was expired!
                response = render(request, 'index.html', context)
                return response

            if status == 400:
                # session was invalid!
                response = render(request, '400.html', { 'issue': 'InvalidJWTSignature' })
                return response

        response = render(request, 'index.html', context)
        ett = random_str(22)
        pl, tk, pk = self.setJWT(ett)

        setCookie(response, 'SSKY', pk)
        setCookie(response, 'SSID', tk)

        return response

    def getJWT(self, tk: str):
        def decode(options: dict = None):
            return jwt.decode(tk, self.__SECRET_KEY, ['HS256'], options)

        try:
            pl = decode()
            return 200, pl
        except jwt.exceptions.ExpiredSignatureError:
            pl = decode({ 'verify_signature': False })
            return 410, pl
        except jwt.exceptions.InvalidSignatureError:
            pl = decode({ 'verify_signature': False })
            return 400, None

    def setJWT(self, entity: str, user_token: str = '', id: int = 1, key: bytes = __SECRET_KEY.encode()):
        t = math.floor(datetime.now().timestamp())
        pl = {
            'iss': 'https://phucharm.store',
            'exp': t + 1800,
            'iat': t,
            'jti': id,
            'kid': str(uuid.uuid4()),
            'ett': entity,
            'utk': user_token
        }
        tk = jwt.encode(pl, self.__SECRET_KEY, 'HS256')
        pk = hash_secret(key, str(pl))
        return pl, tk, pk
