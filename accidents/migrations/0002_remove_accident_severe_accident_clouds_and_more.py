# Generated by Django 4.0.4 on 2022-06-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accidents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accident',
            name='severe',
        ),
        migrations.AddField(
            model_name='accident',
            name='clouds',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='humidity',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='incident_cause',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='accident',
            name='incident_cost',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='accident',
            name='incident_type',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='accident',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='license_number',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='accident',
            name='long',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='pressure',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='road_condition',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='accident',
            name='temp',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='visibility',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='weather_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='accident',
            name='wind_speed',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='accident',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='accident',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
