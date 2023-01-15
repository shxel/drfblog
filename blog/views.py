from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSerializer
from .permissions import BlogPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class BlogView(ModelViewSet):
    '''
    You can perform CRUD operations on Blogs in this view
    as well as search, filter and order
    '''
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filterset_fields = ['author',]
    ordering_fields = ['date',]
    ordering = ['-date',]
    search_fields = [
        'title',
        'body',
        'author__name',
    ]

    # seting permission for this view
    def get_permissions(self):
        if self.action in ['create',]:
            permission_classes = [IsAuthenticated]
        elif self.action in ['destroy', 'partial_update', 'update']:
            permission_classes = [BlogPermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


class BlogLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        blog = Blog.objects.get(id=pk)
        if blog != None:
            if user not in blog.likes.all():
                blog.likes.add(user)
                message = 'You liked this blog'
            else:
                blog.likes.remove(user)
                message = 'You unliked this blog'
        else:
            message = 'not find'
        return Response({'message':message})


class BlogSavedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        blog = Blog.objects.get(id=pk)
        if blog != None :
            if user not in blog.saved.all():
                blog.saved.add(user)
                message = 'You saved this blog'
            else:
                blog.saved.remove(user)
                message = 'You saved this blog'
        else:
            message = 'not find'
        return Response({'massage':massage})

