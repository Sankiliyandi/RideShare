# Generated by Django 4.0.6 on 2023-01-26 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0002_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerRide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('leavingfrom', models.TextField()),
                ('goingto', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.user')),
            ],
        ),
    ]
