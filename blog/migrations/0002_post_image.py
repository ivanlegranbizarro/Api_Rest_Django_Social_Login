# Generated by Django 3.2 on 2021-04-20 18:19

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='posts/default.png', null=True, upload_to=blog.models.upload_to),
        ),
    ]
