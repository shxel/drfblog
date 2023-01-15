from .models import Coments
from .serializers import ComentsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ComentView(ModelViewSet):
    '''
    You can perform CRUD operations on comments in this view
    '''
    model = Coments
    serializer_class = ComentsSerializer
    queryset = Coments.objects.all()

    # seting permission for this view
    def get_permissions(self):
        if self.action in ['create',]:
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'partial_update', 'update']:
            permission_classes = [ComentsPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class ComentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        coment = Coments.objects.get(id=pk)
        if coment != None:
            if user not in coment.likes.all():
                coment.likes.add(user)
                message = 'You liked this coment'
            else:
                coment.likes.remove(user)
                message = 'You unliked this coment'
        else:
            message = 'not find'
        return Response(massage)


class ComentUnLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        coment = Coments.objects.get(id=pk)
        if coment != None:
            if user not in coment.nulikes.all():
                coment.nulikes.add(user)
                message = 'You liked this coment'
            else:
                coment.nulikes.remove(user)
                message = 'You unliked this coment'
        else:
            message = 'not find'
        return Response(massage)

