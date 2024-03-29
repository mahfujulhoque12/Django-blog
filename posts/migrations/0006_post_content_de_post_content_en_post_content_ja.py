# Generated by Django 4.2.9 on 2024-01-10 10:33

from django.db import migrations
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_content_de_remove_post_content_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_de',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ja',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
    ]
