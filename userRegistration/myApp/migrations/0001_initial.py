# Generated by Django 5.0.1 on 2024-06-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('mobileno', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('collegename', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('emailaddress', models.CharField(max_length=50)),
            ],
        ),
    ]