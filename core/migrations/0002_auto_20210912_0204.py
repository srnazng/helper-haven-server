# Generated by Django 3.1.1 on 2021-09-12 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, default='', max_length=255)),
                ('first_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(blank=True, default='', max_length=255)),
                ('gender', models.CharField(blank=True, default='', max_length=10)),
                ('dob', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=255)),
                ('city', models.CharField(blank=True, default='', max_length=255)),
                ('state', models.CharField(blank=True, default='', max_length=255)),
                ('zip', models.CharField(blank=True, default='', max_length=255)),
                ('skills', models.CharField(blank=True, default='', max_length=1000)),
                ('link', models.URLField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
    ]
