from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Products, ProductsType


class ProductsSerializer(serializers.ModelSerializer):
    """
    Serializer class for Pets model
    """

    class Meta:
        model = Products
        fields = '__all__'

    def create_product(self, validated_data):
        name = self.data.get('name')
        quantity = self.data.get('quantity')
        price = self.data.get('price')
        product_type_id = self.data.get('product_type')

        product_type = ProductsType.objects.get(id=product_type_id)

        try:
            product = Products(
                name=name,
                quantity=quantity,
                price=price,
                product_type=product_type
            )

            product.save()

            return {
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "price": product.price,
                "product_type": {
                    "id": product.product_type.id,
                    "type_name": product.product_type.type_name,
                    "date_created": product.product_type.date_created,
                    "date_updated": product.product_type.date_updated,
                }
            }
        except Exception as e:
            raise e

        # if product_type:
        #     product = Products(
        #         name=name,
        #         quantity=quantity,
        #         price=price,
        #         product_type=product_type
        #     )

        #     product.save()

        #     return {
        #         "id": product.id,
        #         "name": product.name,
        #         "quantity": product.quantity,
        #         "price": product.price,
        #         "product_type": {
        #             "id": product.product_type.id,
        #             "type_name": product.product_type.type_name,
        #             "date_created": product.product_type.date_created,
        #             "date_updated": product.product_type.date_updated,
        #         }
        #     }



class ProductsTypeSerializer(serializers.ModelSerializer):
    """
    Serializer class for Pets model
    """

    class Meta:
        model = ProductsType
        fields = '__all__'

    def create_productsType(self, validated_data):
        type_name = self.data.get('type_name')
        date_created = self.data.get('date_created')
        date_updated = self.data.get('date_updated')

        productType = ProductsType(
            type_name=type_name,
            date_created=date_created,
            date_updated=date_updated
        )

        productType.save()

        return {
            "type_name": productType.type_name,
            "date_created": productType.date_created,
            "date_updated": productType.date_updated
        }