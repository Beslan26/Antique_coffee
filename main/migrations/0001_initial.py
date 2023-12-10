# Generated by Django 4.2.7 on 2023-12-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True)),
            ],
        ),
    ]
