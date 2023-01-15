from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserView(ModelViewSet):
    '''
    You can perform CRUD operations and register on users in this view
    '''
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # seting permission for this view
    def get_permissions(self):
        if self.action in ['destroy', 'partial_update', 'update', 'detail']:
            permission_classes = [UserPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]
        
    def perform_create(self, serializer):
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()


class UserFolowView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        myuser = User.objects.get(id=pk)
        if myuser != None and myuser.is_active:
            if user not in myuser.folower.all():
                myuser.folower.add(user)
                message = 'You followed this user'
            else:
                myuser.folower.remove(user)
                message = 'You unfollowed this user'
        else:
            message = 'not find'
        return Response(massage)


class UserNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        myuser = User.objects.get(id=pk)
        if myuser != None and myuser.is_active:
            if user not in myuser.notifications.all():
                myuser.notifications.add(user)
                message = "You have turned on this user's notification"
            else:
                myuser.notifications.remove(user)
                message = "You have turned off this user's notification"
        else:
            message = 'not find'
        return Response(massage)
