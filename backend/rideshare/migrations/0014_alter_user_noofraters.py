# Generated by Django 4.0.6 on 2023-04-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0013_alter_user_noofraters_alter_user_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='noOfRaters',
            field=models.FloatField(),
        ),
    ]
