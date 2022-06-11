from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class HomeViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({
            'Ok': True
        })
