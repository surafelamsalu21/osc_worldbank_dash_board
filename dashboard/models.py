from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DebtEducationData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    external_debt = models.FloatField()
    education_expenditure = models.FloatField()

    def __str__(self):
        return f"{self.country.name} - {self.year}"


class DebtData(models.Model):
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    debt = models.FloatField()


class EducationData(models.Model):
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    expenditure = models.FloatField()
