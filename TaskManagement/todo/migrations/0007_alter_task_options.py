# Generated by Django 5.0.1 on 2024-01-07 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_time']},
        ),
    ]
