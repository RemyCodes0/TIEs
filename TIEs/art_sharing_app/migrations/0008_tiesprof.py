# Generated by Django 4.2.3 on 2023-08-02 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_sharing_app', '0007_alter_event_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TIEsProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='logo')),
            ],
        ),
    ]