# Generated by Django 3.1.1 on 2020-09-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registraion',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
