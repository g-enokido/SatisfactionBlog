# Generated by Django 2.2.5 on 2019-10-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191011_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_icon',
            field=models.ImageField(blank=True, null=True, upload_to='profile_icons/', verbose_name='アイコン'),
        ),
    ]