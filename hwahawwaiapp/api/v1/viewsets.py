from rest_framework import authentication
from hwahawwaiapp.models import UDObshiyttah
from .serializers import UDObshiyttahSerializer
from rest_framework import viewsets


class UDObshiyttahViewSet(viewsets.ModelViewSet):
    serializer_class = UDObshiyttahSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UDObshiyttah.objects.all()
