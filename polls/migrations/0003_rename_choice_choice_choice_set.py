# Generated by Django 4.0.6 on 2022-07-29 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choise_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='choice_set',
        ),
    ]
