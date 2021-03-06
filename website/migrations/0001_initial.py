# Generated by Django 2.1.3 on 2018-11-26 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('accessory_url', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('item_url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('pic_url', models.CharField(max_length=200)),
                ('clothes_name', models.CharField(max_length=100)),
                ('clothes_detail', models.CharField(max_length=200)),
                ('accessories', models.ManyToManyField(to='website.Accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender', models.CharField(choices=[('M', 'man'), ('W', 'woman')], max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Gender'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Type'),
        ),
    ]
