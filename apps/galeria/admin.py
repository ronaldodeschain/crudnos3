from django.contrib import admin
from apps.galeria.models import Fotografia

#Crud de administrador dentro do site
# Register your models here.
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publicada",)
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("categoria","publicada","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10


admin.site.register(Fotografia,ListandoFotografias)
