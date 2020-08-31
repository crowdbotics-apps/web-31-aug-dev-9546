from rest_framework import serializers
from homeidkwhato.models import Hesoyam


class HesoyamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hesoyam
        fields = "__all__"
