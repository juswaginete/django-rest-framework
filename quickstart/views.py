from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pets
from quickstart.serializers import PetsSerializer


class PetsView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, requet, format=None):
        """
        GET endpoint to list all pets in Pets model/table
        """
        pets = Pets.objects.all()
        serializer = PetsSerializer(pets, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        POST endpoint for creating a pet in Pets model/table
        """
        serializer = PetsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.create_pet(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
