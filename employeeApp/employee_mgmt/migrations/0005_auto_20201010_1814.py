# Generated by Django 2.2.16 on 2020-10-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_mgmt', '0004_auto_20201010_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='manager',
            new_name='manager_name',
        ),
    ]
