# Generated by Django 5.1.4 on 2024-12-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_gender_alter_member_registration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='member',
            name='LastName',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
