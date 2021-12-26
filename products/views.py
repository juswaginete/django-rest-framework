from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, ProductsType
from products.serializer import ProductsSerializer, ProductsTypeSerializer


class ProductsView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, requet, format=None):
        """
        GET endpoint to list all pets in Pets model/table
        """
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        POST endpoint for creating a pet in Pets model/table
        """
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.create_product(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsTypeView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, requet, format=None):
        """
        GET endpoint to list all pets in Pets model/table
        """
        productsType = ProductsType.objects.all()
        serializer = ProductsTypeSerializer(productsType, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        POST endpoint for creating a pet in Pets model/table
        """
        serializer = ProductsTypeSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.create_productsType(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

