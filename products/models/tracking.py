from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import AuditableModel, UniqueIDClass
from .product import Product


class Tracking(AuditableModel, UniqueIDClass):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    latitude = models.FloatField(
        validators=[MaxValueValidator(90), MinValueValidator(-90)]
    )
    longitude = models.FloatField(
        validators=[MaxValueValidator(180), MinValueValidator(-180)]
    )
    elevation = models.FloatField()

    class Meta:
        db_table = 'tracking'
