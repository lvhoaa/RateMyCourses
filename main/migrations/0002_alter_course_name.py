# Generated by Django 4.1.7 on 2023-12-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]