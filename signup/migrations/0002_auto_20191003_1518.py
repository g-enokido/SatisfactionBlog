# Generated by Django 2.2.5 on 2019-10-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]