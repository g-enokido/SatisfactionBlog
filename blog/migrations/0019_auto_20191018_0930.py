# Generated by Django 2.2.5 on 2019-10-18 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191018_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='pictures/'),
        ),
    ]
