# Generated by Django 4.2 on 2023-05-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oders_name', models.CharField(blank=True, max_length=15, null=True)),
                ('oders_quantity', models.IntegerField(blank=True, max_length=15, null=True)),
                ('oders_discount', models.IntegerField(blank=True, max_length=15, null=True)),
                ('oders_address', models.TextField(blank=True, max_length=15, null=True)),
                ('oders_place_at', models.TextField(blank=True, max_length=15, null=True)),
                ('oders_time', models.TimeField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='date_or_birth',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]