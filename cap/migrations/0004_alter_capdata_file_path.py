# Generated by Django 4.1.3 on 2022-12-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0003_remove_capdata_file_path2_alter_capdata_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capdata',
            name='file_path',
            field=models.FileField(default='', upload_to='static/files'),
        ),
    ]