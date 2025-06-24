from django.contrib import admin
from django.urls import path, include
from .api_v1 import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
]
