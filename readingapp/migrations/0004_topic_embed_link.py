# Generated by Django 2.1.2 on 2018-11-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingapp', '0003_topic_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='embed_link',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
