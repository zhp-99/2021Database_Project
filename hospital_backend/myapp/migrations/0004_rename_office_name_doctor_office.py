# Generated by Django 4.0 on 2021-12-23 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_office_name_doctor_office_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='office_name',
            new_name='office',
        ),
    ]