# Generated by Django 4.1.3 on 2022-11-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.IntegerField()),
                ('language', models.CharField(choices=[('ukrainian', 'ukrainian'), ('english', 'english'), ('deutsh', 'deutsh')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fiction', models.CharField(max_length=30)),
                ('novels', models.CharField(max_length=30)),
                ('detective', models.CharField(max_length=30)),
                ('adventure', models.CharField(max_length=30)),
                ('fairy_tales', models.CharField(max_length=30)),
            ],
        ),
    ]