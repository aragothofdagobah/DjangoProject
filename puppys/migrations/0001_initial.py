# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToyPoodle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tp_name', models.CharField(max_length=70)),
                ('tp_description', models.CharField(max_length=500)),
                ('tp_pci', models.ImageField(upload_to='pic_folder/')),
            ],
        ),
    ]
