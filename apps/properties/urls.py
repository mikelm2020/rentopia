from django.urls import path, include
from api import routers

urlpatterns = [
    path('', include(routers.router.urls)),
]