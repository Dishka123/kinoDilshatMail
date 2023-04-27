# Generated by Django 4.1.7 on 2023-04-03 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineering', '0002_alter_car_model_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='component',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='model',
        ),
        migrations.DeleteModel(
            name='Line',
        ),
        migrations.RemoveField(
            model_name='order',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='model',
        ),
        migrations.DeleteModel(
            name='Car_model',
        ),
        migrations.DeleteModel(
            name='Component',
        ),
        migrations.DeleteModel(
            name='Composition',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
