# Generated by Django 4.0.4 on 2022-07-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0006_anime_fecha_de_carga'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha_de_carga',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='fecha_de_carga',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
