# Generated by Django 4.2.1 on 2023-07-22 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_part_bicycle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='name',
            new_name='partname',
        ),
    ]