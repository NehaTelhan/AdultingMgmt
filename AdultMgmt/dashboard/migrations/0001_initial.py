# Generated by Django 2.0.5 on 2018-05-27 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('bill_type', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('comment', models.TextField(blank=True, null=True)),
                ('paid_by', models.TextField()),
            ],
        ),
    ]
