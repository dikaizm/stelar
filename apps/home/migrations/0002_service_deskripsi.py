# Generated by Django 4.1.7 on 2023-03-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='deskripsi',
            field=models.CharField(default=str, max_length=100),
            preserve_default=False,
        ),
    ]