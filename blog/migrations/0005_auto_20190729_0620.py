# Generated by Django 2.2.3 on 2019-07-29 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%y%m%d/<django.db.models.query_utils.DeferredAttribute object at 0x10554bfd0>'),
        ),
    ]
