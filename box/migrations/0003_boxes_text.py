# Generated by Django 4.0.4 on 2022-05-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_boxes_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxes',
            name='text',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
