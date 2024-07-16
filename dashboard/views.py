from rest_framework import viewsets
from .models import Country, DebtEducationData
from .serializers import CountrySerializer, DebtEducationDataSerializer
from django.shortcuts import render


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DebtEducationDataViewSet(viewsets.ModelViewSet):
    queryset = DebtEducationData.objects.all()
    serializer_class = DebtEducationDataSerializer


def index(request):
    return render(request, 'index.html')
