from django.db import models

class Elements(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='имя',
                            help_text='напишите имя')
    percent = models.FloatField(max_length=200,
                            verbose_name='процент',
                            help_text='напишите процент')
    image = models.ImageField()



    def __str__(self):
        return f'{self.name}- {self.percent}'


class Alloys(models.Model):
    name = models.CharField(max_length=200,
        verbose_name='имя',
        help_text='напишите имя')
    elements = models.ManyToManyField(Elements)
    description = models.TextField(verbose_name='Описaние',
        help_text='Напишите описание')
    images = models.ImageField()

    def __str__(self):
        return self.name

