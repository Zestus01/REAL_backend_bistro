# Generated by Django 4.1.3 on 2022-11-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_item_title_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='spice_level',
            field=models.CharField(choices=[('', ''), ('🌶️', '🌶️'), ('🌶️🌶️', '🌶️🌶️'), ('🌶️🌶️🌶️', '🌶️🌶️🌶️'), ('🌶️🌶️🌶️🌶️', '🌶️🌶️🌶️🌶️'), ('🌶️🌶️🌶️🌶️🌶️', '🌶️🌶️🌶️🌶️🌶️')], default='', max_length=12),
        ),
    ]