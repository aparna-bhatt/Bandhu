# Generated by Django 2.2 on 2020-06-23 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bandhuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('activity_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('disaster_type', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=800)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('slug', models.SlugField()),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bandhuapp.Profile')),
            ],
            options={
                'verbose_name_plural': 'Charities',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=13, verbose_name='Contact Number')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitywork.Charity')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bandhuapp.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='ankurayan/%Y')),
                ('approved', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charitywork.Activity')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitywork.Charity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='charity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charitywork.Charity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='volunteers',
            field=models.ManyToManyField(to='charitywork.Volunteer'),
        ),
    ]
