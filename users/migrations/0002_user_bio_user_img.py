# Generated by Django 4.2.3 on 2023-07-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='users/profile_picture'),
        ),
    ]