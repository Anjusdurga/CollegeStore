# Generated by Django 4.2.7 on 2023-11-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_alter_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='materials',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
