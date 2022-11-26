from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=254)
    body = serializers.CharField()
    image = serializers.ImageField()

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("name must be 3 char")

