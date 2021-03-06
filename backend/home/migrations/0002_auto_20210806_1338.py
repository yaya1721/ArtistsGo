# Generated by Django 3.2.6 on 2021-08-06 05:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
