# Generated by Django 4.0.2 on 2022-05-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMaterias', '0003_pelicula_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='estreno',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='estrenos'),
        ),
    ]
