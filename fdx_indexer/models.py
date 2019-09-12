from django.db import models
from django.utils.timezone import now

class indexedSite(models.Model):
    domain = models.CharField(max_length=512,  default="", unique=True, verbose_name="Сайт")
    start_url = models.CharField(max_length=512,  default="", unique=True, verbose_name="Начальный адрес а протоколом")
    robotstxt = models.CharField(max_length=2048,  default="", verbose_name="robots txt")
    sitemapxml = models.CharField(max_length=512,  default="", verbose_name="адрес sitemap.xml")
    createtime = models.DateTimeField(default=now, verbose_name="Дата создания", help_text="Здесь если что а не в сети")
    lastupdatetime = models.DateTimeField(default=now, verbose_name="Последний обход")
    is_indexed = models.BooleanField(default=False, verbose_name="Проиндексировано?")

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайты"


class indexedURLs(models.Model):
    site = models.ForeignKey(indexedSite, default=None, blank=True, null=True, verbose_name="Сайт", on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=1024,  default="", unique=True, verbose_name="Url")
    is_indexed = models.BooleanField(default=False, verbose_name="Проиндексировано?")
    createtime = models.DateTimeField(default=now, verbose_name="Дата создания", help_text="Здесь если что а не в сети")
    lastupdatetime = models.DateTimeField(default=now, verbose_name="Последний обход")

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"