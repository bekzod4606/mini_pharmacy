# Generated by Django 5.2 on 2025-04-11 05:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=21, validators=[django.core.validators.RegexValidator(message='Please provide a valid phone number.', regex='^\\+998([0-9][0-9]|99)\\d{7}$')])),
                ('quantity', models.IntegerField()),
                ('delivery_address', models.TextField()),
                ('payment_status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicine')),
            ],
        ),
    ]
