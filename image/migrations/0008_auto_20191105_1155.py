# Generated by Django 2.2.5 on 2019-11-05 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_auto_20191105_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
