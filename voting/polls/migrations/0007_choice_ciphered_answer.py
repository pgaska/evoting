# Generated by Django 2.1.4 on 2019-01-19 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190119_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='ciphered_answer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]