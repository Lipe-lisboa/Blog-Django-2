# Generated by Django 5.0.1 on 2024-01-31 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_metalink_data_create'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MetaLink',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
    ]