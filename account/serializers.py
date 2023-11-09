from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'body', 'image',
                'follower', 'notifications', 'password',
                'is_active', 'is_superuser', 'is_admin', 'is_staff',
                'last_login']

        extra_kwargs = {
                        'password':{'write_only':True},
                        'id':{'read_only':True},
                        'is_active':{'read_only':True},
                        'is_superuser':{'read_only':True},
                        'is_admin':{'read_only':True},
                        'is_staff':{'read_only':True},
                        'last_login':{'read_only':True},
                        }
