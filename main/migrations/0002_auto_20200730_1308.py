# Generated by Django 3.0.8 on 2020-07-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='socialLink',
            field=models.URLField(max_length=256),
        ),
    ]