# Generated by Django 3.2.9 on 2021-11-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_letter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='pokemon_imgs'),
        ),
    ]