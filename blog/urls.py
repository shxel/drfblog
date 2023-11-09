from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('blog', views.BlogView, basename='blogs')

urlpatterns = [
    path('like/<pk>/', views.BlogLikeView.as_view()),
    path('saved/<pk>/', views.BlogSavedView.as_view()),
    path('', include(router.urls))
]
