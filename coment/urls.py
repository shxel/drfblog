from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', views.ComentView, basename='coments')
urlpatterns = [
    path('comment-unlike/<pk>/', views.ComentUnLikeView.as_view()),
    path('comment-like/<pk>/', views.ComentLikeView.as_view()),
    path('', include(router.urls))
]
