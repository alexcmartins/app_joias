# Generated by Django 4.1.2 on 2022-10-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='image_contact',
            field=models.ImageField(upload_to='media/images/%Y/%m/%d/'),
        ),
    ]
