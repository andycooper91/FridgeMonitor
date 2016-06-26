# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kindCode', models.CharField(max_length=200)),
                ('kindDescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userFirstName', models.CharField(max_length=200)),
                ('userLastName', models.CharField(max_length=200)),
                ('userMiddleName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='kind',
            field=models.ForeignKey(to='Monitor.Kind'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to='Monitor.User'),
        ),
    ]
