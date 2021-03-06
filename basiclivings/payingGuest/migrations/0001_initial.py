# Generated by Django 3.0.2 on 2020-04-04 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('amenities_id', models.AutoField(primary_key=True, serialize=False)),
                ('amenities_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('no_of_beds', models.PositiveIntegerField(default=0)),
                ('vacant_beds', models.PositiveIntegerField(default=0)),
                ('rent_per_bed', models.PositiveIntegerField(default=0)),
                ('deposit', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('available_from', models.DateTimeField()),
                ('amenities', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=20)),
                ('special_instruction', models.CharField(blank=True, max_length=400, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('exp_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
                ('area_id', models.ForeignKey(db_column='area_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Area')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('watchlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='payingGuest.Room')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'watchlist',
            },
        ),
        migrations.CreateModel(
            name='RoomsVendorPayment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_beds', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('date_of_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='payingGuest.Room')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rooms_vendor_payment',
            },
        ),
        migrations.CreateModel(
            name='RoomsBookingDetail',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='payingGuest.Room')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rooms_booking_details',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.ImageField(default='', upload_to='payingGuest/images/')),
                ('room_id', models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='payingGuest.Room')),
            ],
            options={
                'db_table': 'room_images',
            },
        ),
    ]
