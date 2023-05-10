
from django.urls import path
from .views import install


urlpatterns = [
    path('', install.home, name="install")
]