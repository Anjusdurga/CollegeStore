# Generated by Django 4.2.7 on 2023-11-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
