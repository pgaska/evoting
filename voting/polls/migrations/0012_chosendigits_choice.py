# Generated by Django 2.1.4 on 2019-01-21 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20190121_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='chosendigits',
            name='Choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Choice'),
        ),
    ]
