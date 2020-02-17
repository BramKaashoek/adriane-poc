# Generated by Django 3.0.3 on 2020-02-17 11:06

from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "fixtures")

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_movie_rating'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]