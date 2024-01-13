from django.contrib import admin

from apps.entrada.models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id_tp_residuos",
        "id_cluster",
        "data",
        "valor",
    ]
    list_filter = ["id_tp_residuos", "id_cluster", "data"]
    search_fields = ["id_tp_residuos__nome", "id_cluster__nome", "data"]
    list_per_page = 15


admin.site.register(Entrada, EntradaAdmin)
