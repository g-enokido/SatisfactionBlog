# Generated by Django 2.2.5 on 2019-10-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20191001_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog_id',
            field=models.IntegerField(default=0),
        ),
    ]