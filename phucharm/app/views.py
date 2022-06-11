from .session import Session

# Create your views here.
class ReverseAngular(Session):
    def loader(self, request):
        return self._loader(request, {
            'title': 'PhuCharm Tester: Render Template'
        })
