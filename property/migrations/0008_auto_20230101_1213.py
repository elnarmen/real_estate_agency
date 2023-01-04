# Generated by Django 2.2.24 on 2022-12-31 18:59
import phonenumbers
from django.db import migrations


def fill_owner_pure_phone_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    flat_objs = Flat.objects.all()

    for flat_obj in flat_objs.iterator():
        flat_obj.owner_pure_phone = phonenumbers.parse(
            flat_obj.owners_phonenumber, 'RU'
        )
        if phonenumbers.is_valid_number(flat_obj.owner_pure_phone):
            flat_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20221231_2026'),
    ]

    operations = [
        migrations.RunPython(fill_owner_pure_phone_field)
    ]



