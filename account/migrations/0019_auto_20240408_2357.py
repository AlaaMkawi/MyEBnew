# Generated by Django 3.0.14 on 2024-04-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_delete_parentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pediatrician',
            name='PediatricianId',
        ),
    ]
