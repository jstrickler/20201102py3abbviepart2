# Generated by Django 3.1.2 on 2020-10-29 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tate_core', '0006_auto_20201028_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(default='', help_text="Artist's full name", max_length=256),
            preserve_default=False,
        ),
    ]
