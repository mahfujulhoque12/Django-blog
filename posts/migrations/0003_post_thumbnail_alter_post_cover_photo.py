# Generated by Django 4.2.9 on 2024-01-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_thumbnail_post_cover_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='POST_thumbnail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='POST_cover_photo'),
        ),
    ]