# Generated by Django 3.0.5 on 2023-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_doctorleave_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorleave',
            name='leave_day',
            field=models.DateField(),
        ),
    ]