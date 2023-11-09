from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('comment', views.CommentView, basename='comments')
urlpatterns = [
    path('comment-unlike/<pk>/', views.CommentUnLikeView.as_view()),
    path('comment-like/<pk>/', views.CommentLikeView.as_view()),
    path('', include(router.urls))
]
