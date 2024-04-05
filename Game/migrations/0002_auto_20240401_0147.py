# Generated by Django 3.2.3 on 2024-03-31 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alloys',
            name='description',
            field=models.TextField(help_text='Напишите описание', verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='AlloyElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(help_text='Напишите процент', verbose_name='Процент')),
                ('alloy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game.alloys')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game.elements')),
            ],
        ),
        migrations.AlterField(
            model_name='alloys',
            name='elements',
            field=models.ManyToManyField(through='Game.AlloyElements', to='Game.Elements'),
        ),
    ]
