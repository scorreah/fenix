# Generated by Django 4.0 on 2023-03-25 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
            options={
                'verbose_name': 'Project owner',
                'verbose_name_plural': 'Project owners',
            },
        ),
    ]