from django.urls import path,include
from .views import hello
import shop

urlpatterns = [
    path('', hello),
]
