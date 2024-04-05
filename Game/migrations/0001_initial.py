# Generated by Django 3.2.3 on 2024-03-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='напишите имя', max_length=200, verbose_name='имя')),
                ('percent', models.FloatField(help_text='напишите процент', max_length=200, verbose_name='процент')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Alloys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='напишите имя', max_length=200, verbose_name='имя')),
                ('description', models.TextField(help_text='Напишите описание', verbose_name='Описaние')),
                ('images', models.ImageField(upload_to='')),
                ('elements', models.ManyToManyField(to='Game.Elements')),
            ],
        ),
    ]