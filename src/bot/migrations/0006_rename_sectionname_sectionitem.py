# Generated by Django 5.0.1 on 2024-02-24 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_section_sectionname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SectionName',
            new_name='SectionItem',
        ),
    ]