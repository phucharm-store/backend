from datetime import datetime
from django.shortcuts import render
from libs.format import hash_secret
from libs.random import random_str
import jwt, uuid, math

# Create and Manage your JWT Session here.
class Session:
    __SECRET_KEY = 'secret'

    def _loader(self, request, context):
        print(self.setJWT(random_str(22)))
        return render(request, 'index.html', context)

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
