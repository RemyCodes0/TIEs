# Generated by Django 4.2.3 on 2023-08-03 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_sharing_app', '0010_rename_tiesprof_tieslogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile', upload_to='profile'),
        ),
    ]