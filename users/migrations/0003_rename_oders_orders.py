# Generated by Django 4.2 on 2023-05-15 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_oders_alter_students_date_or_birth'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oders',
            new_name='Orders',
        ),
    ]