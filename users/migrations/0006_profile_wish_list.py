# Generated by Django 3.1.2 on 2021-01-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20201201_1914'),
        ('users', '0005_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wish_list',
            field=models.ManyToManyField(blank=True, default=None, related_name='wish_list', to='jobs.Job'),
        ),
    ]
