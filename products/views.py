from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, ProductsType
from products.serializer import ProductsSerializer, ProductsTypeSerializer

from django.http import Http404
from rest_framework import status



class ProductsView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, request, format=None):
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

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)

        except Products.DoesNotExist:
            return Response({
                'error': 'True',
                'message': 'Product not found'
            }, status=status.HTTP_404_NOT_FOUND)
            raise Http404
            

    def get(self, request, pk, format=None):
        """
        GET endpoint to list all pets in Pets model/table
        """
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsTypeView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, request, format=None):
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

