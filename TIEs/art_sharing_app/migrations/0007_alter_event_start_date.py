# Generated by Django 4.2.3 on 2023-07-30 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_sharing_app', '0006_alter_like_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]