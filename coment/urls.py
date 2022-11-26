from django.urls import path, include
from .views import ComentsView
from rest_framework import routers
app_name='coment'
router = routers.SimpleRouter()
router.register('coment', ComentsView, basename='coments')
urlpatterns = [
    path('', include(router.urls))
]
