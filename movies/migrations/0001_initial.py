# Generated by Django 2.1.2 on 2018-10-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=200)),
                ('movie_description', models.CharField(max_length=2000)),
                ('movie_director', models.CharField(max_length=1000)),
                ('movie_year', models.CharField(max_length=6)),
            ],
        ),
    ]
