# Generated by Django 4.2.1 on 2023-05-14 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddTodo',
            new_name='Post',
        ),
    ]
