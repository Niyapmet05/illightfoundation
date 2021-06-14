# Generated by Django 3.2.3 on 2021-06-11 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=1)),
                ('birth_date', models.DateField()),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('instagram', models.CharField(max_length=120, null=True)),
                ('facebook', models.CharField(max_length=120, null=True)),
                ('tweeter', models.CharField(max_length=120, null=True)),
                ('website', models.CharField(max_length=120, null=True)),
                ('province', models.CharField(max_length=30, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('sector', models.CharField(max_length=30, null=True)),
                ('cell', models.CharField(max_length=30, null=True)),
                ('village', models.CharField(blank=True, max_length=30, null=True)),
                ('street', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.TextField(default='no bio...')),
                ('avatar', models.ImageField(default='no_picture.png', upload_to='avatar')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
