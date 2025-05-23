# Generated by Django 5.1.6 on 2025-04-16 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0016_merge_20250416_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='document',
            name='mockup_image',
        ),
        migrations.RemoveField(
            model_name='document',
            name='preview_image',
        ),
        migrations.CreateModel(
            name='HeaderFooterImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('header', models.ImageField(blank=True, null=True, upload_to='documents/previews/')),
                ('footer', models.ImageField(blank=True, null=True, upload_to='documents/previews/')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='documents/previews/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_footer_images', to='customadmin.document')),
            ],
        ),
    ]
