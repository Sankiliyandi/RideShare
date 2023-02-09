# Generated by Django 4.0.6 on 2023-01-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0005_remove_offerride_datetime_offerride_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerARide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emai_id', models.EmailField(max_length=254)),
                ('uname', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('leavingfrom', models.CharField(max_length=100)),
                ('goingto', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='offerRide',
        ),
    ]