# Generated by Django 3.1.2 on 2020-10-21 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=36, unique=True)),
                ('author', models.CharField(default='', max_length=36, unique=True)),
                ('description', models.TextField(blank=True, max_length=256)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('is_available', models.BooleanField(default=False)),
                ('published', models.DateField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
