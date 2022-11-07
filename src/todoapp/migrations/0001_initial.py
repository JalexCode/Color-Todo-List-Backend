# Generated by Django 4.0.2 on 2022-03-08 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked', models.BooleanField()),
                ('title', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=100)),
                ('category', models.BooleanField()),
                ('priority', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=5), django.core.validators.MinValueValidator(limit_value=1)])),
                ('datetime', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'ordering': ['datetime'],
            },
        ),
    ]
