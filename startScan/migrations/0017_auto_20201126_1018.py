# Generated by Django 3.0.7 on 2020-11-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0016_scannedhost_date_discovered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scannedhost',
            old_name='date_discovered',
            new_name='discovered_date',
        ),
    ]
