# Generated by Django 3.2.12 on 2022-03-14 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20220309_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='checked',
            new_name='isCompleted',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
    ]
