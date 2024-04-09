# Generated by Django 5.0.3 on 2024-03-24 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_workshopsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopsummary',
            name='psychologist_name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='workshopsummary',
            name='workshop_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
