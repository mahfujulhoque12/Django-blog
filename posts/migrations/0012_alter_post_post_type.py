# Generated by Django 4.2.9 on 2024-01-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_summary_alter_post_summary_de_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('RESEARCH', 'Research'), ('SERVICES', 'Services'), ('PRODUCTS', 'Products'), ('NEWS', 'News'), ('DATABASE', 'Database')], max_length=250),
        ),
    ]
