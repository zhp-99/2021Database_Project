# Generated by Django 2.2.14 on 2021-12-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211222_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=32)),
                ('office_name', models.CharField(max_length=30)),
            ],
        ),
    ]