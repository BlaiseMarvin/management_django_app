# Generated by Django 4.2.2 on 2023-06-28 10:34

from django.db import migrations, models
import intern_data.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(null=True, upload_to=intern_data.models.InternProfile.profile_photo_upload_to)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('university', models.CharField(max_length=255)),
            ],
        ),
    ]
