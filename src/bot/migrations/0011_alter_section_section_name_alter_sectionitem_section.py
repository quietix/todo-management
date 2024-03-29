# Generated by Django 5.0.1 on 2024-02-24 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0010_alter_sectionitem_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sectionitem',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.section'),
        ),
    ]
