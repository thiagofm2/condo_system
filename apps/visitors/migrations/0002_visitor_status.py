# Generated by Django 5.0 on 2023-12-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='status',
            field=models.CharField(choices=[('WAITING', 'Waiting for authorization'), ('VISITING', 'Visiting'), ('LEAVE', 'Visitor left')], default='WAITING', max_length=8, verbose_name='Status of visitor'),
        ),
    ]
