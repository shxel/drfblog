from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('coment/', include('coment.urls')),
    path('', include('blog.urls')),
]
