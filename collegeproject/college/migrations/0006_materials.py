# Generated by Django 4.2.7 on 2023-11-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_purposes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]