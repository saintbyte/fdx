from django.db import models


class Peoples(models.Model):
    name = models.CharField(max_length=1024, verbose_name='Название персоны')

    class Meta:
        verbose_name_plural = 'Персоны'
        verbose_name = 'Персона'


class Pages(models.Model):
    url = models.URLField(verbose_name="Адрес")

    class Meta:
        verbose_name_plural = 'Веб страницы'
        verbose_name = 'Веб страница'


class Images(models.Model):
    page = models.ForeignKey(Pages, on_delete=models.CASCADE, related_name="image2page", blank=True, null=True,
                             verbose_name="Веб страница")
    url = models.URLField(verbose_name="Адрес")

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'


class Faces(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE, related_name="face2image", blank=True, null=True,
                              verbose_name="Картинка")
    people = models.ForeignKey(Peoples, on_delete=models.CASCADE, related_name="face2people", blank=True, null=True,
                               verbose_name="Персона")
    top = models.IntegerField(blank=0, default=0, verbose_name='Top')
    right = models.IntegerField(blank=0, default=0, verbose_name='Right')
    bottom = models.IntegerField(blank=0, default=0, verbose_name='Bottom')
    left = models.IntegerField(blank=0, default=0, verbose_name='Left')

    class Meta:
        verbose_name_plural = 'Лица'
        verbose_name = 'Лицо'
