# Generated by Django 4.2.11 on 2024-04-13 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Load', '0002_loadedboxdata_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loadedboxdata',
            old_name='loadSeuqence',
            new_name='loadSequence',
        ),
    ]
