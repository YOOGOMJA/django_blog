# Generated by Django 2.2.3 on 2019-07-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190729_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%y/%m/%d/%h'),
        ),
    ]
