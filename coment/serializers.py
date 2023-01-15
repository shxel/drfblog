from rest_framework import serializers
from .models import Coments


class ComentsSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    def get_author(self, instance):
        return str(instance.author.name)

    class Meta:
        model = Coments
        fields = '__all__'

        extra_kwargs = {
                        'id': {'read_only': True},
                        'date': {'read_only': True},
                        }

    def __call__(self, value, body):
        if len(value) < 1:
            message = 'you must add 1 char'
            raise serializers.ValidationError(message)