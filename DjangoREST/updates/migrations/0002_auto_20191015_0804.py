# Generated by Django 2.2.6 on 2019-10-15 08:04

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='update',
            managers=[
                ('class_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='update',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
