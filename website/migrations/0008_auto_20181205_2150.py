# Generated by Django 2.1.3 on 2018-12-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20181205_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='mencolor',
            name='color7',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='mencolor',
            name='color8',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='womencolor',
            name='color7',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='womencolor',
            name='color8',
            field=models.CharField(default='', max_length=7),
        ),
    ]