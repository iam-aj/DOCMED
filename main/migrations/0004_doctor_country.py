# Generated by Django 2.0 on 2020-11-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201129_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='country',
            field=models.CharField(default='NOT AVAIALBE', max_length=255),
        ),
    ]