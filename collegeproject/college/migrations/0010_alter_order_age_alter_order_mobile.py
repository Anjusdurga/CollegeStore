# Generated by Django 4.2.7 on 2023-11-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_alter_order_dob_alter_order_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
