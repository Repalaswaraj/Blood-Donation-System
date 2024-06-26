# Generated by Django 4.2.11 on 2024-04-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_name', models.CharField(max_length=50, null=True)),
                ('Patient_email', models.EmailField(max_length=50, null=True)),
                ('Patient_age', models.IntegerField(null=True)),
                ('Patient_bloodGroup', models.CharField(max_length=10, null=True)),
                ('Patient_Unit', models.IntegerField(null=True)),
                ('Patient_dat', models.IntegerField(null=True)),
                ('Patient_disease', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
