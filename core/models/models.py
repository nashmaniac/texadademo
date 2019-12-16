from django.db import models
from model_utils.models import SoftDeletableModel, SoftDeletableManager, TimeStampedModel
# Create your models here.


class AuditableModel(TimeStampedModel, SoftDeletableModel):

    objects = models.Manager()
    soft_manager = SoftDeletableManager()

    class Meta:
        abstract = True
