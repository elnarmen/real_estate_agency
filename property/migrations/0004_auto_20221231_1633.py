# Generated by Django 2.2.24 on 2022-12-31 13:21

from django.db import migrations
from django.db.models import F


def choose_building_characteristic(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=F('construction_year') >= 2015)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(choose_building_characteristic)
    ]
