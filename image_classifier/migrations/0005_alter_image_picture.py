# Generated by Django 4.1 on 2022-10-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_classifier', '0004_alter_image_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to='classifier'),
        ),
    ]