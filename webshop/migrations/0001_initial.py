# Generated by Django 3.2.1 on 2021-05-05 00:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('created_by', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('date_added', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webshop.product')),
            ],
        ),
    ]
