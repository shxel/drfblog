from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.CurrentUserDefault()
    

    def get_author(self, instance):
        return str(instance.author.name)

    class Meta:
        model = Comments
        fields = ['reply', 'id', 'reply_to_reply', 'body',
                'date', 'author',  'likes', 'un_likes', 'blog']
        extra_kwargs = {
                        'id':{'read_only':True},
                        'date':{'read_only':True},
                        }
