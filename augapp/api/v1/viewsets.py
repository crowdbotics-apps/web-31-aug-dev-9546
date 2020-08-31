from rest_framework import authentication
from augapp.models import Au31app
from .serializers import Au31appSerializer
from rest_framework import viewsets


class Au31appViewSet(viewsets.ModelViewSet):
    serializer_class = Au31appSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Au31app.objects.all()
