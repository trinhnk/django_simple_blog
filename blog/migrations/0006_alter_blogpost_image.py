# Generated by Django 3.2.8 on 2021-10-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/static/blog/img/post'),
        ),
    ]
