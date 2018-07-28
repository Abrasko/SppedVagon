# Generated by Django 2.0.7 on 2018-07-28 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_based',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_name', models.CharField(max_length=80, unique=True)),
                ('original_user_name', models.CharField(max_length=80, null=True)),
                ('public_name', models.CharField(max_length=60)),
                ('user_email', models.EmailField(max_length=255, verbose_name='email adress')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_of_register', models.DateField(default=django.utils.timezone.now)),
                ('user_city', models.CharField(default='None', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
