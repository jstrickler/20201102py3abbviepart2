# Generated by Django 3.1.3 on 2020-11-02 19:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wombat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID of this Wombat record', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'wombat',
                'verbose_name_plural': 'wombats',
                'db_table': 'wombats',
            },
        ),
    ]
