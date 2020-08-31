from rest_framework import authentication
from homemidelname.models import Huskywhitecolour
from .serializers import HuskywhitecolourSerializer
from rest_framework import viewsets


class HuskywhitecolourViewSet(viewsets.ModelViewSet):
    serializer_class = HuskywhitecolourSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Huskywhitecolour.objects.all()
