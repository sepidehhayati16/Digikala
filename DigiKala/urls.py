
from django.contrib import admin
from django.urls import path
from shop.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/', hello),
]
