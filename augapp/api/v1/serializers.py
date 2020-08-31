from rest_framework import serializers
from augapp.models import Au31app


class Au31appSerializer(serializers.ModelSerializer):
    class Meta:
        model = Au31app
        fields = "__all__"
