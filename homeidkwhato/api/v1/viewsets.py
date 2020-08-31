from rest_framework import authentication
from homeidkwhato.models import Hesoyam
from .serializers import HesoyamSerializer
from rest_framework import viewsets


class HesoyamViewSet(viewsets.ModelViewSet):
    serializer_class = HesoyamSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Hesoyam.objects.all()
