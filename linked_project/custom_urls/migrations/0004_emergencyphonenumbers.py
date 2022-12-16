# Generated by Django 4.1.4 on 2022-12-13 22:19

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('custom_urls', '0003_emergencyname'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyPhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(max_length=200, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='US')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emergency_phone', to='custom_urls.urls')),
            ],
        ),
    ]