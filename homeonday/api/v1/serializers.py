from rest_framework import serializers
from homeonday.models import Mayh9jius


class Mayh9jiusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mayh9jius
        fields = "__all__"
