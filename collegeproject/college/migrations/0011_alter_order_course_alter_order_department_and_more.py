# Generated by Django 4.2.7 on 2023-11-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_alter_order_age_alter_order_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='department',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
    ]
