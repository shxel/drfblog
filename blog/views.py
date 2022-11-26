from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSerializer
from .permissions import BlogPermission

class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermission]

    def get_queryset(self):
        author = self.kwargs['author']
        if author is not None :
            queryset = Blog.objects.filter(author=author)
        return queryset

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermission]

    def get_queryset(self):
        author = self.request.query_params.get('author')
        if author is not None :
            queryset = Blog.objects.filter(author=author)
        return queryset