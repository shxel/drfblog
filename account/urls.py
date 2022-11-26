from django.urls import path, include
from .views import profile, folow, UserView
from rest_framework import routers
router = routers.SimpleRouter()
router.register('update', UserView, basename='update')
app_name='account'
urlpatterns = [
    path('profiel/<pk>', profile, name='profile'),
    path('folow/<pk>', folow, name='folow'),
    path('', include(router.urls))
]
