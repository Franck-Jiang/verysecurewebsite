# Generated by Django 4.2.1 on 2023-05-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AlterField(
            model_name='patient',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
