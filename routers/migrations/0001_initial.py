# Generated by Django 3.0.7 on 2022-01-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='router_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sapid', models.CharField(max_length=18)),
                ('Hostname', models.CharField(max_length=14)),
                ('Loopback', models.CharField(max_length=10)),
                ('Mac_address', models.CharField(max_length=17)),
            ],
        ),
    ]
