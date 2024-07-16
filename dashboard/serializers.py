from rest_framework import serializers
from .models import Country, DebtEducationData


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DebtEducationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtEducationData
        fields = '__all__'
