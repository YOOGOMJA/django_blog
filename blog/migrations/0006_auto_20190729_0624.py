# Generated by Django 2.2.3 on 2019-07-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190729_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%y%m%d/<django.db.models.query_utils.DeferredAttribute object at 0x105b5ff90>'),
        ),
    ]
