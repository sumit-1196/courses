# Generated by Django 3.1.3 on 2021-01-24 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycourse', '0005_auto_20210123_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learning',
            old_name='learning',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='prerequisite',
            old_name='prerequisite',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tagline',
            old_name='tagline',
            new_name='description',
        ),
    ]