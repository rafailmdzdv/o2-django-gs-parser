# Generated by Django 4.1.7 on 2023-03-21 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieselfueltypes',
            name='df_arctica_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieselfueltypes',
            name='df_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieselfueltypes',
            name='df_taneko_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieselfueltypes',
            name='df_winter_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
