# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('ClientId', models.CharField(max_length=10)),
                ('Email', models.CharField(primary_key=True, max_length=100, serialize=False)),
                ('ClientName', models.CharField(max_length=150)),
                ('Password', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='UserMasterTable',
            fields=[
                ('UserId', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('UserEmail', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=50)),
                ('UserCompany', models.CharField(max_length=100)),
                ('UserPassword', models.CharField(max_length=20)),
                ('UserActiveStatus', models.IntegerField()),
                ('UserCreatedBy', models.CharField(max_length=50)),
                ('UserCreatedDate', models.DateField(max_length=8)),
                ('UserUpdatedBy', models.CharField(max_length=50)),
                ('UserUpdatedDate', models.DateField(max_length=8)),
            ],
        ),
    ]
