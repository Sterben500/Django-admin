# Generated by Django 3.2.13 on 2022-06-13 20:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crud_main', '0004_applicaitonshasservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='overall',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('number_of_server_used', models.IntegerField()),
                ('total_storage_used', models.IntegerField()),
            ],
        ),
    ]