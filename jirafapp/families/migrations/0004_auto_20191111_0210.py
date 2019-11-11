# Generated by Django 2.2.6 on 2019-11-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0003_auto_20191110_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kidheight',
            name='percentile',
        ),
        migrations.AddField(
            model_name='kidheight',
            name='percentile_oms',
            field=models.CharField(default=0, max_length=10, verbose_name='Percentile Oms'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kidheight',
            name='percentile_sap',
            field=models.CharField(default=0, max_length=10, verbose_name='Percentile Sap'),
            preserve_default=False,
        ),
    ]
