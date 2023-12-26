# Generated by Django 5.0 on 2023-12-26 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concierge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_name', models.CharField(max_length=200, verbose_name="Visitor's name")),
                ('document', models.CharField(max_length=11, verbose_name="Visitor's document (CPF)")),
                ('birthdate', models.DateField(verbose_name="Visitor's Birthdate")),
                ('home_number', models.PositiveSmallIntegerField(verbose_name='Number of the house')),
                ('license_plate', models.CharField(blank=True, max_length=8, null=True, verbose_name='Vehicle license plate')),
                ('arrival_time', models.DateTimeField(auto_now_add=True, verbose_name='Arrival time on lobby')),
                ('departure_time', models.DateTimeField(blank=True, null=True, verbose_name='Departure time of condo')),
                ('authorization_time', models.DateTimeField(blank=True, null=True, verbose_name='The time when visitor is authorized to entry')),
                ('responsible_resident', models.CharField(blank=True, max_length=200, verbose_name='Name of the resident responsible of authorize the visitor')),
                ('concierge_responsible', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concierge.concierge', verbose_name='Consierge responsible for register')),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
                'db_table': 'visitor',
            },
        ),
    ]