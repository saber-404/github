# Generated by Django 2.0.6 on 2018-06-19 07:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=500),
        ),
    ]
