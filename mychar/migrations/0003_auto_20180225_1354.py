# Generated by Django 2.0.2 on 2018-02-25 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mychar', '0002_auto_20180225_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileparams',
            name='city',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='profileparams',
            name='date_of_register',
            field=models.DateField(default=datetime.datetime(2018, 2, 25, 10, 54, 17, 583297, tzinfo=utc)),
        ),
    ]