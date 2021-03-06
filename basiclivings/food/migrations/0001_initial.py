# Generated by Django 3.0.2 on 2020-04-04 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('mess_id', models.AutoField(primary_key=True, serialize=False)),
                ('mess_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mess',
            },
        ),
        migrations.CreateModel(
            name='Tiffin_types',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'tiffin_types',
            },
        ),
        migrations.CreateModel(
            name='MessVendorPayment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True)),
                ('exp_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('mess_id', models.ForeignKey(db_column='mess_id', on_delete=django.db.models.deletion.CASCADE, to='food.Mess')),
                ('package_id', models.ForeignKey(db_column='package_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Packages')),
            ],
            options={
                'db_table': 'mess_vendor_payment',
            },
        ),
        migrations.CreateModel(
            name='Mess_bookings',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('mess_id', models.ForeignKey(db_column='mess_id', on_delete=django.db.models.deletion.CASCADE, to='food.Mess')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mess_bookings',
            },
        ),
        migrations.CreateModel(
            name='Food_types',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=2048)),
                ('price', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], default='Veg', max_length=20)),
                ('mess_id', models.ForeignKey(db_column='mess_id', on_delete=django.db.models.deletion.CASCADE, to='food.Mess')),
                ('tiffin_id', models.ForeignKey(db_column='tiffin_id', on_delete=django.db.models.deletion.CASCADE, to='food.Tiffin_types')),
            ],
            options={
                'db_table': 'food_types',
            },
        ),
    ]
