# Generated by Django 2.2.8 on 2020-01-11 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='images')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(choices=[('Graphite', 'Graphite'), ('Modern', 'Modern'), ('Metal', 'Metal'), ('Oversize', 'Oversize'), ('Wood', 'Wood')], on_delete=django.db.models.deletion.PROTECT, to='products.Category')),
            ],
        ),
    ]
