from django.urls import include, path

from .views import PetsView

urlpatterns = [
    path('', PetsView.as_view(), name="pets")
]