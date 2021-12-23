from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Pets


class PetsSerializer(serializers.ModelSerializer):
    """
    Serializer class for Pets model
    """

    class Meta:
        model = Pets
        fields = '__all__'

    def create_pet(self, validated_data):
        name = self.data.get('name')
        gender = self.data.get('gender')
        animal_type = self.data.get('animal_type')

        pet = Pets(
            name=name,
            gender=gender,
            animal_type=animal_type
        )

        pet.save()

        return {
            "id": pet.id,
            "name": pet.name,
            "gender": pet.gender,
            "animal_type": pet.animal_type
        }