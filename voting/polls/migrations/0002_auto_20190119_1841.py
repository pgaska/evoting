# Generated by Django 2.1.4 on 2019-01-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='private_key',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='public_key_x',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='public_key_y',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]