# Generated by Django 4.2.7 on 2023-11-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
