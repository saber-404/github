# Generated by Django 2.0 on 2018-07-27 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180727_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
    ]
