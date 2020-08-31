from rest_framework import serializers
from hwahawwaiapp.models import UDObshiyttah


class UDObshiyttahSerializer(serializers.ModelSerializer):
    class Meta:
        model = UDObshiyttah
        fields = "__all__"
