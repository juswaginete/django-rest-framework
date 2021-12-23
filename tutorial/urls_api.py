from django.urls import include, path

from rest_framework.routers import SimpleRouter

profile_router = SimpleRouter()

urlpatterns = [
    path('pet/', include('quickstart.urls_pets'))
]