# Generated by Django 4.0.4 on 2022-07-04 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0007_pelicula_fecha_de_carga_serie_fecha_de_carga'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='donde_ver',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
