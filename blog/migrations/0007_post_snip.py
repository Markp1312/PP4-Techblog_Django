# Generated by Django 4.0 on 2022-01-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_name_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snip',
            field=models.CharField(default='Click to read post', max_length=150),
        ),
    ]
