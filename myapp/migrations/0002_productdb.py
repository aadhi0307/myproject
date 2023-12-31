# Generated by Django 4.1.7 on 2023-05-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('pname', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('pimage', models.ImageField(blank=True, null=True, upload_to='product')),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
