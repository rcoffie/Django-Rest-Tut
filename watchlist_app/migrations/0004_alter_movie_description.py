# Generated by Django 3.2.5 on 2021-09-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]