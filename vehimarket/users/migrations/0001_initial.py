# Generated by Django 4.2.6 on 2023-10-31 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_fname', models.TextField(db_column='firstname', default='null', max_length=50)),
                ('u_lname', models.TextField(db_column='lastname', default='null', max_length=50)),
                ('u_dob', models.DateField(db_column='dateofbirth', default='2023-10-02')),
                ('u_contact', models.CharField(db_column='contactinfo', default='1234567890', max_length=50)),
                ('u_house', models.TextField(db_column='house', default='null', max_length=50)),
                ('u_place', models.TextField(db_column='place', default='null', max_length=50)),
                ('u_pin', models.TextField(db_column='pincode', default='null', max_length=50)),
                ('u_profile', models.ImageField(db_column='profileimage', default='null', upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
