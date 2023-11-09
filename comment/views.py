from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import CommentPermission
from rest_framework.response import Response


class CommentView(ModelViewSet):
    '''
    You can perform CRUD operations on comments in this view
    '''
    model = Comments
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    # set permission for this view
    def get_permissions(self):
        if self.action in ['create',]:
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'partial_update', 'update']:
            permission_classes = [CommentPermission]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]


class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        comment = Comments.objects.get(id=pk)
        message = 'error'
        if comment != None:
            if user not in comment.likes.all():
                comment.likes.add(user)
                message = 'You liked this comment'
            else:
                comment.likes.remove(user)
                message = 'You un liked this comment'
        else:
            message = 'not find'
        return Response(message)


class CommentUnLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        comment = Comments.objects.get(id=pk)
        message = 'error'
        if comment != None:
            if user not in comment.un_likes.all():
                comment.un_likes.add(user)
                message = 'You liked this comment'
            else:
                comment.un_likes.remove(user)
                message = 'You un liked this comment'
        else:
            message = 'not find'
        return Response(message)

