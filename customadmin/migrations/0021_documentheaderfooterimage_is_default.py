# Generated by Django 4.2.18 on 2025-04-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0020_alter_font_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentheaderfooterimage',
            name='is_default',
            field=models.BooleanField(null=True),
        ),
    ]
