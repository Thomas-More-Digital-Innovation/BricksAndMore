# Generated by Django 4.0.4 on 2022-10-18 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_alter_creation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
