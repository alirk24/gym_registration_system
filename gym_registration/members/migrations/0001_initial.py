# Generated by Django 5.1.4 on 2024-12-14 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_in_months', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'مرد'), ('F', ' زن')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('MembershipPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.membershipplan')),
            ],
        ),
    ]