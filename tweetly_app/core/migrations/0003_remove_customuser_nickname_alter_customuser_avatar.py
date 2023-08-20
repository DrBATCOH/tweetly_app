# Generated by Django 4.2.3 on 2023-08-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_populare_default_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(upload_to='media/avatars/'),
        ),
    ]