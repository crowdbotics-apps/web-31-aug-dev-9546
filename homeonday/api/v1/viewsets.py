from rest_framework import authentication
from homeonday.models import Mayh9jius
from .serializers import Mayh9jiusSerializer
from rest_framework import viewsets


class Mayh9jiusViewSet(viewsets.ModelViewSet):
    serializer_class = Mayh9jiusSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Mayh9jius.objects.all()
