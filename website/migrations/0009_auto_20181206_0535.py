# Generated by Django 2.1.3 on 2018-12-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20181205_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menclothes',
            name='category',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='womenclothes',
            name='category',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
