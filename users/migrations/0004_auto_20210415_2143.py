# Generated by Django 3.1.7 on 2021-04-16 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210415_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='languajes',
            new_name='languages',
        ),
    ]
