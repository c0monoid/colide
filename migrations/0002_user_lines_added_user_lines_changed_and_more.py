# Generated by Django 4.0.5 on 2022-11-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lines_added',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='lines_changed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='lines_deleted',
            field=models.IntegerField(default=0),
        ),
    ]
