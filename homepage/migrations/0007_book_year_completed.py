# Generated by Django 3.2.4 on 2021-09-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_journalentry_contents'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year_completed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
