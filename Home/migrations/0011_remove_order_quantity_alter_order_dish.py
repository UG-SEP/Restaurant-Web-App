# Generated by Django 4.0.3 on 2022-04-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_items_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='dish',
            field=models.ManyToManyField(to='Home.items'),
        ),
    ]
