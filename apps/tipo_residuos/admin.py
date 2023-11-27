from django.contrib import admin

from apps.tipo_residuos.models import TipoResiduos


class TipoResiduosAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    list_display_links = ["id", "nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
    list_per_page = 15


admin.site.register(TipoResiduos, TipoResiduosAdmin)
