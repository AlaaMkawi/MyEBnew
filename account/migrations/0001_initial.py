# Generated by Django 5.0.3 on 2024-03-07 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InformationBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('babyage', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('parantId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pediatrician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('PediatricianId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('PsychologistId', models.IntegerField(default=0)),
            ],
        ),
    ]