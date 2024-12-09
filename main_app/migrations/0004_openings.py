# Generated by Django 5.1.3 on 2024-11-26 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Openings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_title', models.CharField(max_length=30)),
                ('Job_description', models.TextField()),
                ('Place', models.CharField(max_length=20)),
                ('wage', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('Employer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.employer')),
            ],
        ),
    ]
