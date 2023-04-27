# Generated by Django 4.2 on 2023-04-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_instrumentalresearch_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentalresearchcard',
            name='instrumental_research',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='mainapp.instrumentalresearch'),
        ),
    ]