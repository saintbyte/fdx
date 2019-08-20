from django.db import models
from .storage import Md5FileSystemStorage
from django.conf import settings
import os
import hashlib
from any_imagefield.models import AnyImageField



def md5_file_name(instance, filename):
    h = instance.md5sum
    basename, ext = os.path.splitext(filename)
    return os.path.join(settings.MEDIA_ROOT, h[0:1], h[1:2], h + ext.lower())


class UploadedImages(models.Model):
    file = AnyImageField("Image", upload_to='searches')
    face_count = models.IntegerField(blank=True, default=0, verbose_name='Face Count')

    def save(self, *args, **kwargs):
        basename, ext = os.path.splitext(self.file.path)
        super(UploadedImages, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Картинки загруженные для поиска'
        verbose_name = 'Картинки загруженные для поиска'

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
    top = models.IntegerField(blank=True, default=0, verbose_name='Top')
    right = models.IntegerField(blank=True, default=0, verbose_name='Right')
    bottom = models.IntegerField(blank=True, default=0, verbose_name='Bottom')
    left = models.IntegerField(blank=True, default=0, verbose_name='Left')

    class Meta:
        verbose_name_plural = 'Лица'
        verbose_name = 'Лицо'
