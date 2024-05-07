# Generated by Django 5.0.4 on 2024-05-07 00:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.UUID('2b8613e5-4c92-4ad0-b8f4-278fe8dca1bd'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.PositiveIntegerField()),
                ('num_bedrooms', models.PositiveIntegerField()),
                ('num_bathrooms', models.PositiveIntegerField()),
                ('property_type', models.CharField(choices=[('AP', 'Apartment'), ('LA', 'Land'), ('HO', 'House')], max_length=2)),
                ('rating_property', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('num_floors', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('num_floors', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('properties.property',),
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='properties.property')),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('properties.property',),
        ),
    ]
