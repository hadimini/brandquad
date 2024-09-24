# Generated by Django 4.0 on 2024-09-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_ip', models.CharField(max_length=32)),
                ('time', models.DateTimeField()),
                ('method', models.CharField(max_length=12)),
                ('url', models.TextField()),
                ('response', models.IntegerField()),
                ('bytes', models.IntegerField()),
            ],
        ),
    ]
