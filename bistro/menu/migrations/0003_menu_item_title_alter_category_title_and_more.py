# Generated by Django 4.1.3 on 2022-11-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_category_id_menu_item_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='cuisine',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
