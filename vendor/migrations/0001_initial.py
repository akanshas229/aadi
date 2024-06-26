# Generated by Django 5.0.4 on 2024-05-04 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('store_description', models.TextField()),
                ('address', models.CharField(max_length=500)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='vendor_logos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='vendor.vendor')),
            ],
        ),
    ]
