# Generated by Django 4.2.5 on 2023-10-07 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blblbl', '0002_alter_comment_options_alter_post_options_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Images',
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
