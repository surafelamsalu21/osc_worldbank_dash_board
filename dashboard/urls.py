

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, DebtEducationDataViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'data', DebtEducationDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
