# Generated by Django 4.0.4 on 2022-04-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('davaci', models.CharField(max_length=50)),
                ('davaci_vekili', models.CharField(max_length=150)),
                ('davali', models.CharField(max_length=100)),
                ('davali_vekili', models.CharField(max_length=150)),
                ('mahkeme', models.CharField(max_length=150)),
                ('esas', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('InProgress', 'InProgress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
                ('case_date', models.DateField()),
                ('due_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'case',
                'verbose_name_plural': 'cases',
            },
        ),
    ]
