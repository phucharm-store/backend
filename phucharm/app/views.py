from django.shortcuts import render

# Create your views here.
class ReverseAngular:
    def loader(self, request):
        return render(request, 'index.html', {
            'title': 'PhuCharm Tester: Render Template'
        })
