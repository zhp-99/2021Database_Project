# Generated by Django 2.2.14 on 2021-12-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211228_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='description',
            field=models.CharField(default='default_description', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='office',
            name='leader_username',
            field=models.CharField(default='default_leader', max_length=32, null=True),
        ),
    ]
