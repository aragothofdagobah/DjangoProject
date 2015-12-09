# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShihTzu',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('Name', models.CharField(max_length=70)),
                ('Description', models.CharField(max_length=500)),
                ('Pic', models.ImageField(upload_to='pic_folder/', default='')),
            ],
        ),
        migrations.RenameField(
            model_name='toypoodle',
            old_name='tp_description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='toypoodle',
            old_name='tp_name',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='toypoodle',
            name='tp_pci',
        ),
        migrations.AddField(
            model_name='toypoodle',
            name='Pic',
            field=models.ImageField(upload_to='pic_folder/', default=''),
        ),
    ]
