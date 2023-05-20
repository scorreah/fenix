# Generated by Django 4.0 on 2023-05-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('NON', '--Elige una--'), ('TEC', 'Tecnología'), ('SCI', 'Ciencia'), ('ART', 'Arte'), ('REA', 'Lectura'), ('HEA', 'Salud'), ('MUS', 'Música')], max_length=3),
        ),
    ]
