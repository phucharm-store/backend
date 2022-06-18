from django.http import HttpResponse

def setCookie(response: HttpResponse, name: str, value: str):
    return response.set_cookie(
        key=name,
        value=value,
        max_age=31536000,
        httponly=True
    )
