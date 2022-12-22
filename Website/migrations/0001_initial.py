# Generated by Django 4.0 on 2021-12-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('team_id', models.IntegerField()),
                ('season_year', models.IntegerField()),
                ('player_id', models.IntegerField()),
            ],
        ),
    ]
