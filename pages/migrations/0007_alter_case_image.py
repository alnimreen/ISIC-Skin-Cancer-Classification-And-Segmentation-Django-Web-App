# Generated by Django 4.2.5 on 2023-10-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_case_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.FileField(upload_to='project/media'),
        ),
    ]