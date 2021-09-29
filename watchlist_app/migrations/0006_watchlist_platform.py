# Generated by Django 3.2.5 on 2021-09-29 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_auto_20210929_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist_app.streamplatform'),
            preserve_default=False,
        ),
    ]
