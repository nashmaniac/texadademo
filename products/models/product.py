from django.db import models
from core.models import AuditableModel

# Create your models here.


class Product(AuditableModel):
    '''
        typically an string id or hash should be used for security purpose. As the example suggests an integer,
        therefor id field is not overidden
    '''
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'products'


