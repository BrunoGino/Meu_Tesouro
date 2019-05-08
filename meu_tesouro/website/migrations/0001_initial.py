# Generated by Django 2.1.7 on 2019-05-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('scraping_date', models.DateField()),
                ('url', models.CharField(max_length=100)),
                ('title_name', models.CharField(max_length=50)),
                ('title_type', models.CharField(max_length=50)),
                ('interest', models.DecimalField(decimal_places=4, max_digits=14)),
                ('interest_type', models.CharField(max_length=50)),
                ('title_value', models.DecimalField(decimal_places=4, max_digits=14)),
                ('minimum_value', models.DecimalField(decimal_places=4, max_digits=14)),
                ('liquidity', models.IntegerField()),
                ('total_time', models.IntegerField()),
                ('ending_date', models.DateField()),
                ('emitter', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('emitter_risk_level', models.IntegerField()),
                ('emitter_risk_level_type', models.CharField(max_length=50)),
                ('fgc', models.IntegerField()),
                ('ir', models.IntegerField()),
            ],
            options={
                'db_table': 'title',
            },
        ),
    ]
