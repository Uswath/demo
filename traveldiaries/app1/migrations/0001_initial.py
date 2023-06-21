# Generated by Django 4.2 on 2023-05-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='traveldiaries/img')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timg', models.ImageField(blank=True, null=True, upload_to='traveldiaries/timg')),
                ('tname', models.CharField(max_length=30)),
                ('tdesc', models.CharField(max_length=200)),
            ],
        ),
    ]
