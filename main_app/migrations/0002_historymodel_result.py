# Generated by Django 3.2.6 on 2021-10-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historymodel',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
