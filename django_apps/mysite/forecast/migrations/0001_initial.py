# Generated by Django 4.0 on 2022-10-21 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etf_ticker', models.CharField(max_length=10)),
                ('etf_name', models.CharField(max_length=200)),
                ('index_name', models.CharField(max_length=200)),
                ('cape', models.CharField(max_length=10)),
                ('fwd_return_forecast', models.CharField(max_length=10)),
                ('index_ticker', models.CharField(max_length=10)),
            ],
        ),
    ]
