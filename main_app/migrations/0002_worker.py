# Generated by Django 5.1.3 on 2024-11-23 05:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=3)),
                ('DOB', models.DateField()),
                ('Address', models.TextField()),
                ('Ph_no', models.CharField(max_length=10)),
                ('Job_category', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=30)),
                ('Preffered_location', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract')], max_length=10)),
                ('document', models.FileField(upload_to='documents/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Worker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
