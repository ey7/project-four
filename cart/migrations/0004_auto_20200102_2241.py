# Generated by Django 2.2.8 on 2020-01-02 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20191231_1604'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
    ]