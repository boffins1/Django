# Generated by Django 4.1.2 on 2022-11-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopping1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('price', models.IntegerField()),
                ('read', models.IntegerField()),
                ('thumbnail', models.URLField()),
            ],
        ),
    ]
