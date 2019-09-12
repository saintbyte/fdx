from django.contrib import admin
from .models import indexedSite, indexedURLs


class indexedSiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(indexedSite, indexedSiteAdmin)


class indexedURLsAdmin(admin.ModelAdmin):
    pass


admin.site.register(indexedURLs, indexedURLsAdmin)
