from rest_framework import serializers
from users.models import Model


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"
