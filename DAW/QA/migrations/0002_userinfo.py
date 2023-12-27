# Generated by Django 4.2 on 2023-12-19 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.BooleanField()),
                ('age', models.TextField(max_length=20)),
                ('status', models.TextField(max_length=20)),
                ('levelOfEducation', models.TextField(max_length=150)),
                ('profession', models.TextField(max_length=150)),
                ('annualRevenue', models.TextField(max_length=250)),
                ('idUser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
