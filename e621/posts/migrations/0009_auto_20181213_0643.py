# Generated by Django 2.1.3 on 2018-12-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20181209_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingestlog',
            name='artists_deleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ingestlog',
            name='sources_deleted',
            field=models.IntegerField(default=0),
        ),
    ]
