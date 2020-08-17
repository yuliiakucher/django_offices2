from rest_framework import serializers
from .models import OfficeModel, CityModel


class CustomCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ('city',)


class OfficeSerializer(serializers.ModelSerializer):
    # city = CustomCitySerializer(many=True)

    class Meta:
        model = OfficeModel
        fields = ('__all__')
