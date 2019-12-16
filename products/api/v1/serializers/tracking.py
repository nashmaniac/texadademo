from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator

class TrackingCreateSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
    latitude = serializers.FloatField(
        validators=[MaxValueValidator(90), MinValueValidator(-90)]
    )
    longitude = serializers.FloatField(
        validators=[MaxValueValidator(180), MinValueValidator(-180)]
    )
    elevation = serializers.FloatField()