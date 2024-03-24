from django.urls import path
from .views import index, blog

urlpatterns = [
    path('', index),
    path('<id>/', blog),
]
