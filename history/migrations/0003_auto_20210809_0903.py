# Generated by Django 2.2.24 on 2021-08-09 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_history_action_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('-created',)},
        ),
    ]
