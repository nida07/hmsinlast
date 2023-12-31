# Generated by Django 3.0.5 on 2023-11-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_doctorleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('is_public', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
