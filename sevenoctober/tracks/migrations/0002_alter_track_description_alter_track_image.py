# Generated by Django 4.2.6 on 2023-10-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tracks/images/'),
        ),
    ]
