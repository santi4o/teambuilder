# Generated by Django 3.1.7 on 2021-05-28 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20210526_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('service', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('team_performance', 'Desempeño de equipo'), ('personality', 'Personalidad')], max_length=17),
        ),
    ]
