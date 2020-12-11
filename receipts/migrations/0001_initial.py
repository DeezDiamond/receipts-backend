# Generated by Django 3.1.4 on 2020-12-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('receipt_image', models.ImageField(upload_to='images/')),
                ('items', models.CharField(max_length=1000)),
            ],
        ),
    ]
