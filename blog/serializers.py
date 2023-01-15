from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    

    def get_author(self, instance):
        return str(instance.author.name)

    class Meta:
        model = Blog
        fields = ['id', 'image', 'author', 'title',
                'saved', 'date',  'likes', 'body']
        extra_kwargs = {
                        'id': {'read_only': True},
                        'date': {'read_only': True},
                        }