# Generated by Django 2.1.3 on 2018-12-11 07:25

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_one', models.CharField(max_length=255)),
                ('line_two', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.PositiveSmallIntegerField()),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('number', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('lab', models.BooleanField(default=False)),
                ('honors', models.BooleanField(default=False)),
                ('writing', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
                ('online', models.BooleanField(default=False)),
                ('graduate', models.BooleanField(default=False)),
                ('min_credit_hours', models.PositiveSmallIntegerField()),
                ('max_credit_hours', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.PositiveSmallIntegerField(unique=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Building')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=1)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=3, validators=[base.models.validate_lowercase])),
                ('max_seats', models.PositiveSmallIntegerField()),
                ('filled_seats', models.PositiveSmallIntegerField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Campus')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Course')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Location')),
                ('meeting_times', models.ManyToManyField(to='base.MeetingTime')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.CharField(max_length=4, unique=True)),
                ('long', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject_area',
            field=models.ManyToManyField(to='base.SubjectArea'),
        ),
        migrations.AddField(
            model_name='campus',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Location'),
        ),
        migrations.AddField(
            model_name='address',
            name='building',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Building'),
        ),
    ]