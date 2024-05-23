# Generated by Django 4.2.11 on 2024-05-22 18:59

import apps.owners.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='owner_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('rating_user', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(blank=True, default='perfil.jpg', null=True, upload_to=apps.owners.models.get_upload_path, verbose_name='Profiles')),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Propietario',
                'verbose_name_plural': 'Propietarios',
            },
        ),
    ]
