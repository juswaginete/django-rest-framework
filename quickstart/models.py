from django.db import models

optional = {
    'null': True,
    'blank': True,
}


# Create your models here.
class Pets(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )

    PET_TYPE = (
        ('C', 'Cat'),
        ('D', 'Dog'),
    )

    name = models.CharField(max_length=255, **optional)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, **optional)
    animal_type = models.CharField(max_length=2, choices=PET_TYPE, **optional)