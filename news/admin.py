from django.contrib import admin
from .models import *

# Register your models here.

class KategoriSlug(admin.ModelAdmin):
    readonly_fields=[
        'slug'
    ]

admin.site.register(Kategori, KategoriSlug)
admin.site.register(Berita)