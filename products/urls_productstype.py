from django.urls import include, path

from .views import ProductsTypeView

urlpatterns = [
    path('', ProductsTypeView.as_view(), name="productstype")
]