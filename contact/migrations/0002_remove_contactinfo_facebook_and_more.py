# Generated by Django 5.1.1 on 2024-09-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='twitter',
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
