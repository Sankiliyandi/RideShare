# Generated by Django 4.0.6 on 2023-02-12 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0008_rename_data_offeraride_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNo',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]