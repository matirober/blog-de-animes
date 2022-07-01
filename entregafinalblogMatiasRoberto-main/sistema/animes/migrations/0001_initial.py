# Generated by Django 4.0.4 on 2022-06-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('episodios', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('autor', models.CharField(max_length=100)),
                ('duracion', models.FloatField(verbose_name=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('autor', models.CharField(max_length=100)),
                ('duracion', models.FloatField(verbose_name=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('episodios', models.IntegerField()),
                ('estado', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripcion')),
                ('autor', models.CharField(max_length=100)),
                ('duracion', models.FloatField(verbose_name=0.0)),
            ],
        ),
    ]
