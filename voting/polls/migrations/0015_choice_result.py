# Generated by Django 2.1.4 on 2019-01-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_chosendigits_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='result',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
