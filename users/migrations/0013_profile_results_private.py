# Generated by Django 3.1.7 on 2021-05-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210516_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='results_private',
            field=models.BooleanField(default=True),
        ),
    ]
