# Generated by Django 4.2.1 on 2023-05-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_email', models.EmailField(max_length=100)),
                ('doctor_email', models.EmailField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('place', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=10000)),
                ('patient_email', models.EmailField(max_length=100)),
                ('doctor_email', models.EmailField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
