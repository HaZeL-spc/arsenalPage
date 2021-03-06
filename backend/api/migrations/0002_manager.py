# Generated by Django 2.2 on 2020-12-04 08:14

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('year_start', models.IntegerField()),
                ('year_end', models.IntegerField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to=api.models.upload_to, verbose_name='Image')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Team')),
            ],
        ),
    ]
