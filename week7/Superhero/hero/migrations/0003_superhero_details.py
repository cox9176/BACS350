# Generated by Django 3.2.7 on 2021-10-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_superhero_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='details',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]