from django.db import models


class UnderPoint(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = 'Подпункт меню'
        verbose_name_plural = 'Подпункты меню'

    def __str__(self):
        return self.name


class MenuPoint(models.Model):
    name = models.CharField(max_length=30)
    underpoint = models.ManyToManyField(UnderPoint, default='')
    slug = models.SlugField(default='')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=30)
    points = models.ManyToManyField(MenuPoint, default='')
    slug = models.SlugField(default='')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
