import hmac, hashlib

def hash_sha256(i: str):
    return hashlib.sha256(i.encode()).hexdigest()

def hash_sha512(i: str):
    return hashlib.sha512(i.encode()).hexdigest()

def hash_secret(key: bytes, i: str, alg = hashlib.blake2s):
    m = hmac.new(key, digestmod=alg)
    m.update(i.encode())
    return m.hexdigest()
