# Generated by Django 4.1.6 on 2023-02-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_attendancerange'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendanceclass',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendance'},
        ),
    ]
