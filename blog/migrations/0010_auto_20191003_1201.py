# Generated by Django 2.2.5 on 2019-10-03 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_updated_by_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='image.png', null=True, upload_to='pictures/'),
        ),
    ]
