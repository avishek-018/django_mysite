# Generated by Django 2.2.4 on 2019-08-20 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190820_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='turorial_title',
            new_name='tutorial_title',
        ),
    ]