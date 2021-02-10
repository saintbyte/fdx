from django.contrib import admin
from .models import UploadedImages


class UploadedImagesAdmin(admin.ModelAdmin):
    pass


admin.site.register(UploadedImages, UploadedImagesAdmin)