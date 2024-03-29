# Generated by Django 3.2.3 on 2021-07-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='billingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=12)),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipCode', models.CharField(max_length=50)),
            ],
        ),
    ]
