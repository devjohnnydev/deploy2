# Generated by Django 5.1.1 on 2024-09-28 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='user',
            new_name='usuario',
        ),
    ]
