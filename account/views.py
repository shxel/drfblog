from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import redirect

def profile(request, pk):
    if reqest.user.is_authenticated:
        user = User.objects.get(id=pk)
        if request.user.id == user.id:
            serializer = UserSerializer(user)
            return Response(serializer)
        else:
            return redirect('blog:home')
    else:
        return redirect('acount:login')

class UserView(viewsets.ViewSet):
    def update(self, request, pk=None):
        queryset = Coments.objects.all()
        serializser_classes = ComentsSerializer

@api_view(['POST'])
def folow(request, pk):
    user = User.objects.get(id=pk)
    if request.user not in user.folower.all():
        user.folower.add(request.user)
    else:
        user.folower.remove(request.user)
