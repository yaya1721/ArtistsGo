# Generated by Django 3.2.6 on 2021-08-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210806_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='netid',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
