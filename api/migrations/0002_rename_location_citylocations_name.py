# Generated by Django 3.2.9 on 2021-12-08 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citylocations',
            old_name='location',
            new_name='name',
        ),
    ]
