# Generated by Django 4.2 on 2023-04-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumentalresearch',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='instrumentalresearchcategory',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
