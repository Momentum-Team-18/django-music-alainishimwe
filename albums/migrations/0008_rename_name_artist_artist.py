# Generated by Django 4.2.1 on 2023-05-24 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_rename_artist_name_artist_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='name',
            new_name='artist',
        ),
    ]
