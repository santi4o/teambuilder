# Generated by Django 3.1.7 on 2021-05-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20210525_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('personality', 'Personalidad'), ('team_performance', 'Desempeño de equipo')], max_length=17),
        ),
    ]
