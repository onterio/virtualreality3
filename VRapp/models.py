from django.db import models

class Temes(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Items(models.Model):
    temes = models.ForeignKey(Temes,
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/img", default=100, verbose_name="Изображение")
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Пункты'