# Generated by Django 2.2.5 on 2019-10-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20191003_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_detail',
            field=models.TextField(blank=True, null=True, verbose_name='ブログ詳細'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_name',
            field=models.CharField(max_length=200, verbose_name='ブログタイトル'),
        ),
    ]
