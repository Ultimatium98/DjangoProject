# Generated by Django 3.1 on 2020-08-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hash',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='txId',
            field=models.CharField(default=None, max_length=66, null=True),
        ),
    ]