from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Tracking


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


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tracking
        depth = 1
