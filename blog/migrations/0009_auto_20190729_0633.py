# Generated by Django 2.2.3 on 2019-07-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190729_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%y%m%d%h%%m%s/'),
        ),
    ]