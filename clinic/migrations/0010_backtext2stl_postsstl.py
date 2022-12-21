# Generated by Django 4.1.3 on 2022-12-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_delete_postsstl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backtext2stl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Postsstl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
