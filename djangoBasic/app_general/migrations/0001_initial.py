# Generated by Django 4.0.5 on 2022-09-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image_profile', models.ImageField(blank=True, null=True, upload_to='media/profile')),
                ('image_post', models.ImageField(blank=True, null=True, upload_to='media')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
