# Generated by Django 3.1.7 on 2021-03-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20210317_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]