# Generated by Django 4.2.7 on 2024-05-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField()),
                ('secilization', models.CharField(max_length=40)),
            ],
        ),
    ]
