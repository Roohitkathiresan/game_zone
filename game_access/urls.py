from django.contrib import admin
from django.urls import path, include
from games.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('games/', include('games.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]