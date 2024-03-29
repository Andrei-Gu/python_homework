# Generated by Django 4.2 on 2023-04-07 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentalResearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentalResearchCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40, unique=True)),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentalResearchCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_r_description', models.TextField(max_length=2000)),
                ('i_r_price', models.PositiveIntegerField()),
                ('i_r_interesting_fact', models.TextField(blank=True, max_length=2000)),
                ('i_r_preparation', models.ManyToManyField(to='mainapp.preparation')),
                ('instrumental_research', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.instrumentalresearch')),
            ],
        ),
        migrations.AddField(
            model_name='instrumentalresearch',
            name='i_r_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.instrumentalresearchcategory'),
        ),
    ]
