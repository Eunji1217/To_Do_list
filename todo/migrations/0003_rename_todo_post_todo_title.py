# Generated by Django 4.2.1 on 2023-05-14 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_addtodo_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='todo',
            new_name='todo_title',
        ),
    ]
