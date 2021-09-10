# Generated by Django 3.1.1 on 2021-09-10 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('role', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255, unique=True)),
                ('contact_name', models.CharField(blank=True, max_length=30)),
                ('contact_email', models.EmailField(blank=True, max_length=60)),
                ('contact_number', models.CharField(blank=True, max_length=30)),
                ('event_summary', models.CharField(max_length=1000)),
                ('role_description', models.CharField(max_length=1000)),
                ('max_hours', models.PositiveIntegerField(blank=True, default=24, null=True)),
                ('date', models.CharField(blank=True, max_length=255)),
                ('time', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('upcoming', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=255)),
                ('event_name', models.CharField(max_length=255)),
                ('role', models.CharField(blank=True, max_length=1000)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('comments', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]