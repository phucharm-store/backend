import string, random

def random_str(length: int, char: str = string.ascii_letters + string.digits, salt: str = ''):
    r = char + salt
    return ''.join(random.choice(r) for _ in range(length))
