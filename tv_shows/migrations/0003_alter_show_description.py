# Generated by Django 3.2.6 on 2021-08-24 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0002_alter_show_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]