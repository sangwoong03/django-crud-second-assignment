# Generated by Django 4.0.5 on 2022-06-08 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_actormovie_actor_movie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actor_Movie',
            new_name='MovieActor',
        ),
        migrations.AlterModelTable(
            name='movieactor',
            table='movies_actors',
        ),
    ]