# Generated by Django 3.2.14 on 2022-08-03 22:47

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PT_APP', '0002_auto_20220729_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, populate_from='name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]