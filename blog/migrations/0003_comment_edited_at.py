# Generated by Django 5.1.5 on 2025-02-14 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
