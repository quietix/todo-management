# Generated by Django 5.0.1 on 2024-02-24 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_alter_sectionitem_text_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='sectionitem',
            old_name='section_id',
            new_name='section',
        ),
    ]
