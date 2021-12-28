# Generated by Django 4.0 on 2021-12-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=32)),
                ('dName', models.CharField(max_length=32)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('leader_username', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(default='x', max_length=50)),
                ('email', models.CharField(default='未注册', max_length=32)),
                ('realName', models.CharField(default='x', max_length=32)),
                ('gender', models.CharField(default='x', max_length=2)),
                ('birthday', models.DateField(null=True)),
                ('idCardNumber', models.CharField(default='x', max_length=18, unique=True)),
                ('phoneNumber', models.CharField(default='x', max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=32)),
                ('dName', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('medical', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=32)),
                ('dName', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(default='x', max_length=50)),
                ('email', models.CharField(default='未注册', max_length=32)),
                ('realName', models.CharField(default='x', max_length=32)),
                ('gender', models.CharField(default='x', max_length=2)),
                ('birthday', models.DateField(null=True)),
                ('idCardNumber', models.CharField(default='x', max_length=18, unique=True)),
                ('phoneNumber', models.CharField(default='x', max_length=11, unique=True)),
                ('college', models.CharField(default='Peking', max_length=32)),
                ('degree', models.CharField(default='Peking', max_length=32)),
                ('is_leader', models.BooleanField()),
                ('office_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.office')),
            ],
        ),
    ]