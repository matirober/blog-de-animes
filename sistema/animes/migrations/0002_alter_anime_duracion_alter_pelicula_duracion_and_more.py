# Generated by Django 4.0.4 on 2022-06-17 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='duracion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='duracion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='serie',
            name='duracion',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]