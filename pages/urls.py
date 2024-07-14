from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from .views import home, home_redirect, about

urlpatterns = [
    path('', home),
    path('home/', home_redirect),
    path('about/', about),
    path('admin/', admin.site.urls),
    path('account/', include(auth_urls)),
]
