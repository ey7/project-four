# Generated by Django 2.2.8 on 2020-01-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200111_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('graphite', 'Graphite'), ('modern', 'Modern'), ('metal', 'Metal'), ('oversize', 'Oversize'), ('modern', 'Modern')], max_length=100),
        ),
    ]
