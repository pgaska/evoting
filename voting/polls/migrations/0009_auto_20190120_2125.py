# Generated by Django 2.1.4 on 2019-01-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190119_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='chosen_answer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='chosen_key',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]