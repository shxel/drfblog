from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.SimpleRouter()
router.register('user', views.UserView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('follow/<pk>/', views.UserFollowView.as_view()),
    path('notification/<pk>/', views.UserNotificationView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

