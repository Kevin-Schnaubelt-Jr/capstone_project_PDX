# Generated by Django 4.1.4 on 2023-01-09 14:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=200, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('zip_code', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyPhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=200, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_key', models.CharField(max_length=200, unique=True)),
                ('image', models.CharField(max_length=250, null=True)),
                ('dot_options_type', models.CharField(default='extra-rounded', max_length=50)),
                ('dot_options_color', models.CharField(default='#6a1a4c', max_length=50)),
                ('background_options_color', models.CharField(default='#ffffff', max_length=50)),
                ('corner_square_options_type', models.CharField(default='extra-rounded', max_length=50)),
                ('corner_square_options_color', models.CharField(default='#000000', max_length=50)),
                ('corner_dot_options_type', models.CharField(default='extra-rounded', max_length=50)),
                ('corner_dot_options_color', models.CharField(default='#000000', max_length=50)),
            ],
        ),
    ]
