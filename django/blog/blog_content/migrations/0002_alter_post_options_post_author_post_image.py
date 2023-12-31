# Generated by Django 5.0 on 2023-12-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=80, null=True, verbose_name='Blog Author'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images', verbose_name='Blog Image'),
        ),
    ]
