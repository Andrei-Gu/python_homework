# Generated by Django 4.2 on 2023-04-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_instrumentalresearchcard_instrumental_research'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentalresearchcard',
            name='instrumental_research',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.instrumentalresearch'),
        ),
    ]
