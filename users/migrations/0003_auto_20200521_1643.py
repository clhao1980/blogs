# Generated by Django 2.1.15 on 2020-05-21 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200521_1640'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='tb_users',
        ),
    ]
