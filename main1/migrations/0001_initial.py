# Generated by Django 4.2.7 on 2023-11-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('sub_title', models.CharField(help_text='Nima haqidaligini yozing', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Our_studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='our_studio/%Y/%m/%d')),
                ('photo_title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='serive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('sub_title', models.CharField(max_length=20)),
            ],
        ),
    ]