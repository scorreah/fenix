# Generated by Django 4.1.7 on 2023-05-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0004_remove_investing_project_investing_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
