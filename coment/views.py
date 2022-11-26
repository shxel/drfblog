from rest_framework import viewsets
from .models import Coments
from .serializers import ComentsSerializer

class ComentsView(viewsets.ModelViewSet):
    queryset = Coments.objects.all()
    serializser_classes = ComentsSerializer
    filterset_fields = ["author",]
    ordering_fields = ["date",]
    ordering = ["-date",]
    search_fields = [
		"title",
		"body",
		"author__username",
		"author__name",
	]