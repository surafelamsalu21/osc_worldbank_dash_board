# Generated by Django 4.2.14 on 2024-07-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebtData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('debt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('expenditure', models.FloatField()),
            ],
        ),
    ]