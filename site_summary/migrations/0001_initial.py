# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'sites',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('a_value', models.FloatField()),
                ('b_value', models.FloatField()),
                ('site', models.ForeignKey(to='site_summary.Site')),
            ],
            options={
                'db_table': 'site_entries',
            },
            bases=(models.Model,),
        ),
    ]
