# Generated by Django 3.2.5 on 2021-09-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
    ]
