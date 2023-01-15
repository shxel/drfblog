from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', views.UserView, basename='users')

urlpatterns = [
    path('folow/<pk>/', views.UserFolowView.as_view()),
    path('notification/<pk>/', views.UserNotificationView.as_view()),
    path('', include(router.urls))
]

