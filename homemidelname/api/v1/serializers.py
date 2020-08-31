from rest_framework import serializers
from homemidelname.models import Huskywhitecolour


class HuskywhitecolourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huskywhitecolour
        fields = "__all__"
