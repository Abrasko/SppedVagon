# Generated by Django 2.0.7 on 2018-07-28 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mychar', '0002_auto_20180728_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='charphoto',
            name='is_char_photo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='charphoto',
            name='photo_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]