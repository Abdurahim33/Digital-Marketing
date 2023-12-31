# Generated by Django 4.2.7 on 2023-11-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='', verbose_name='contact_us/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'contact_us',
                'verbose_name_plural': 'contact_uses',
            },
        ),
        migrations.RenameModel(
            old_name='main',
            new_name='Home',
        ),
        migrations.RenameModel(
            old_name='serive',
            new_name='service',
        ),
        migrations.DeleteModel(
            name='Our_studio',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'Abouts'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Homes'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'servise', 'verbose_name_plural': 'services'},
        ),
    ]
