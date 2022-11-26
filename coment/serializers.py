from rest_framework import serializers
from .models import Coments

class ComentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coments
        fields = '__all__'

    def __call__(self, value, body):
        if len(value) < 1:
            message = 'you must add 1 char'
            raise serializers.ValidationError(message)