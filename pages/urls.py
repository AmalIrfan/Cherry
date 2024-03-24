from django.urls import path
from .views import home, home_redirect, about

urlpatterns = [
    path('', home),
    path('home/', home_redirect),
    path('about/', about),
]
