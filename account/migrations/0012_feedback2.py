# Generated by Django 5.0.4 on 2024-04-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_pediatricianinfoboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
