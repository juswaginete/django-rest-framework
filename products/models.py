from django.db import models

# Create your models here.

optional = {
    'null': True,
    'blank': True,
}

class ProductsType(models.Model):
    type_name = models.CharField(max_length=255, **optional)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.type_name)


class Products(models.Model):
    name = models.CharField(max_length=255, **optional)
    quantity = models.IntegerField(**optional)
    price = models.DecimalField(max_digits=20, decimal_places=8, **optional)

    product_type = models.ForeignKey(ProductsType, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return(self.name)

